from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.generic import ListView, DetailView

import logging
import requests

from .forms import CarForms
from reservation.models import RezervModel

# API
url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

# api key for Fll Vin
_api_key = "a990fd22-2dfc-46dd-b8cd-061c035bc09c"

DataPackage = "VehicleAndMotHistory"


# header API
headers = {
    'x-api-key': 'LkmZehCC9z96eAkRtthdQ5fD0IAWsLyH9fQrJHSb',
    'Content-Type': 'application/json'
}

engine_service_mapping = {
    0: {'full_service': 150, 'interim_service': 120},
    2000: {'full_service': 170, 'interim_service': 140},
    3000: {'full_service': 180, 'interim_service': 150}
}


@csrf_protect
def HomeView(request):

    if request.method == 'POST':
        form = CarForms(request.POST)

        # check valid data
        if form.is_valid():
            form.save()

            # request post to api
            try:
                res_sms = SMSApi_2(request.POST['tag'])
                tag = request.POST['tag']
                payload = "{\n\t\"registrationNumber\": \"%s\"\n}" % (tag,)
                response = requests.request("POST", url, headers=headers, data=payload)
                res = response.json()

                # not car
                if response.status_code == 400:
                    messages.error(request, 'There is no car')
                    return render(request, 'pages/home.html')

                # car valid ♥
                if response.status_code == 200:
                    engine = response.json()['engineCapacity']
                    register = response.json()['registrationNumber']
                    make = response.json()['make']

                    service_values = {}

                    for key in sorted(engine_service_mapping.keys()):
                        if engine < key:
                            service_values = engine_service_mapping[key]
                            break
                    
                    return render(request, 'pages/detail_car.html',
                                  {'response': res,
                                   'FullService': service_values['full_service'],
                                   'InterimService': service_values['interim_service'],
                                   'register': register,
                                   'make': make,
                                   'res_sms': res_sms,
                                   })

            # not connect internet
            except Exception as e:
                logging.error(e)
                messages.warning(request, 'error internet connect')
                return render(request, 'pages/home.html')

        # not valid | 8 < x
        messages.warning(request, 'Please enter your information correctly')
        return render(request, 'pages/home.html')

    # request get
    return render(request, 'pages/home.html')


def SMSApi_2(tag):

    rvm = tag.upper()

    _Payload = {
        "v": 2,  # Package version
        "api_nullitems": 1,  # Return null items
        "key_vrm": rvm,  # Vehicle registration mark
        "auth_apikey": _api_key  # Set the API Key
    }

    r = requests.get('https://uk1.ukvehicledata.co.uk/api/datapackage/{}'.format(DataPackage),
                     params=_Payload)

    if r.status_code == requests.codes.ok:
        vin = r.json()
        s = vin['Response']['DataItems']['VehicleRegistration']['Vin']
        return s

    else:
        return r.status_code


class FactorListView(ListView):
    model = RezervModel
    template_name = 'pages/list_factor.html'
    context_object_name = 'factors'


class FactorDetailView(DetailView):
    model = RezervModel
    template_name = 'pages/detail_factor.html'
    context_object_name = 'factors'
