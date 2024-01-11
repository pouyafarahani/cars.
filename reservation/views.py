import datetime

from django.contrib import messages
from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view

# import datetime
import urllib.parse
import urllib.request

from .models import *
from .forms import RezervForm

# api key
api_key = "MzYzMDY4Njc0YjRkNmM3NTc5NTg1NzQ1NmI3ODY3NjQ="



def sendSMS(apikey, numbers, sender, message):
    data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
                                   'message': message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.txtlocal.com/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return fr


def Number44(request, phone):
    phone = str(request.POST['PhoneNumber'])
    phone = phone[1:]
    phone = "44" + phone
    return phone


def RezervView(request):
    # request post
    if request.method == 'POST':
        form = RezervForm(request.POST)
        print(form)
        # data valid
        if form.is_valid():

            # 0782452582
            phone1 = int(request.POST['PhoneNumber'][0])
            phone2 = phone1 + 1

            if phone2 == 1:
                phone = str(request.POST['PhoneNumber'])
                PhoneNumber = Number44(request, phone)
                form.save()
                yars = request.POST['sallist']
                moths = request.POST['mahlist']
                day = request.POST['roozlist']
                phone = request.POST['PhoneNumber']
                firs_name = request.POST['Firstname']
                last_name = request.POST['Lastname']

                try:
                    if request.POST['timelist']:
                        time = request.POST['timelist']
                        time = "at " + time
                except:
                    time = str()

                try:
                    resp = sendSMS(
                        'NGY2OTY2Mzg0YzU4NDc0NjQxNzc1MDUxNDE1NzM5MzI=',
                        f'{PhoneNumber}',
                        'Easyfit MOT',
                        f'Hi {firs_name} {last_name} \n Thanks for booking!we look forward to seeing you {time} on {yars}-{moths}-{day}')
                        
                except:
                    messages.success(request, 'Your reservation has been successfully registered')
                    return redirect('reservations:contact')

                messages.success(request, 'Your reservation has been successfully registered')  # valid ♥
                return render(request, 'pages/contact.html')

            else:
                messages.warning(request, 'Your phone number is wrong')  # not valid
                return render(request, 'rezerv.html',
                              {
                                  'FullService': request.session['FullService'],
                                  'InterimService': request.session['InterimService'],
                                  'register': request.session['register'],
                                  'make': request.session['make'],
                              })

        # deta not valid
        else:
            # be har dalili nakhast kar kone barash try mizarim ♥
            try:
                messages.warning(request, 'Your information is not correct')  # not valid
                return render(request, 'rezerv.html',
                              {
                                  'FullService': request.session['FullService'],
                                  'InterimService': request.session['InterimService'],
                                  'register': request.session['register'],
                                  'make': request.session['make'],
                              })

            except ValueError:
                return redirect('pages:home')

    # be har dalili nakhast kar kone barash try mizarim ♥
    try:
        # request get | price service
        request.session['FullService'] = request.GET['FullService']
        request.session['InterimService'] = request.GET['InterimService']
        request.session['register'] = request.GET['register']
        request.session['make'] = request.GET['make']
        return render(request, 'rezerv.html', {'FullService': request.session['FullService'],
                                               'InterimService': request.session['InterimService'],
                                               'register': request.session['register'],
                                               'make': request.session['make'],
                                               })

    except:
        return redirect('pages:home')


# Mohammad

@api_view(['POST'])
def checkyear(request):
    d = datetime.datetime.now()
    mounthnow = int(d.strftime("%m"))
    currentyear = int(datetime.date.today().year)
    year = request.POST['checkyear']
    year = int(year)

    r = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]
    if currentyear == year:
        r = r[mounthnow - 1:]
    else:
        pass
    all_checked=AdminCheckedTime.objects.all()    
    if len(all_checked) >0:
        for i in all_checked:
            
            if i.sallist == "{}-all".format(year):
                r=[]
                
            if "all" in  i.mahlist:   
                if i.mahlist ==  "1-all": 
                    r.remove("January")  
                elif i.mahlist ==  "2-all": 
                    r.remove("February")
                elif i.mahlist ==  "3-all": 
                    r.remove("March")
                elif i.mahlist ==  "4-all": 
                    r.remove("April")
                elif i.mahlist ==  "5-all": 
                    r.remove("May")
                elif i.mahlist ==  "6-all": 
                    r.remove("June")
                elif i.mahlist ==  "7-all": 
                    r.remove("July")
                elif i.mahlist ==  "8-all": 
                    r.remove("August")
                elif i.mahlist ==  "9-all": 
                    r.remove("September")
                elif i.mahlist ==  "10-all": 
                    r.remove("October")
                elif i.mahlist ==  "11-all": 
                    r.remove("November")  
                elif i.mahlist ==  "12-all": 
                    r.remove("December")                                                        
            
                    
                
    return Response({'month': r})


@api_view(['POST'])
def checkmounth(request):
    d = datetime.datetime.now()
    mounthnow = int(d.strftime("%m"))
    daynow = int(datetime.datetime.today().day)
    mounth = request.POST['mounth']
    year = request.POST['year']
    m1 = [1, 3, 5, 6, 7, 8, 10, 12]  # نماینده  ماه هایی  که 31 روز است
    m2 = [4, 9, 11]  # نماینده ماه هایی که 30 روز است

    a = []
    r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31]
    r2 = []
    if int(mounth) in m1:
        pass
    elif int(mounth) in m2:
        r.pop()
    else:
        r.pop()
        r.pop()
    r2 = r
    if mounthnow == int(mounth):
        r = r[daynow - 1:]
        r2 = r

    # حذف روزهایی که کلا تایمش پره
    for k in r:
        book = RezervModel.objects.filter(sallist=year, mahlist=mounth, roozlist=k)

        if len(book) > 9:
            r = r2.remove(k)
    
    all_checked=AdminCheckedTime.objects.all()    
    if len(all_checked) > 0:
        for i in all_checked:
            if int(i.sallist) == int(year) and int(i.mahlist) == int(mounth):
               if "all" in  i.roozlist:   
                if i.roozlist ==  "1-all": 
                    r2.remove(1)  
                elif i.roozlist ==  "2-all": 
                    r2.remove(2)
                elif i.roozlist ==  "3-all": 
                    r2.remove(3)
                elif i.roozlist ==  "4-all": 
                    r2.remove(4)
                elif i.roozlist ==  "5-all": 
                    r2.remove(5)
                elif i.roozlist ==  "6-all": 
                    r2.remove(6)
                elif i.roozlist ==  "7-all": 
                    r2.remove(7)
                elif i.roozlist ==  "8-all": 
                    r2.remove(8)
                elif i.roozlist ==  "9-all": 
                    r2.remove(9)
                elif i.roozlist ==  "10-all": 
                    r2.remove(10)
                elif i.roozlist ==  "11-all": 
                    r2.remove(11)  
                elif i.roozlist ==  "12-all": 
                    r2.remove(12)
                elif i.roozlist ==  "13-all": 
                    r2.remove(13)    
                elif i.roozlist ==  "14-all": 
                    r2.remove(14)    
                elif i.roozlist ==  "15-all": 
                    r2.remove(15)                      
                elif i.roozlist ==  "16-all": 
                    r2.remove(16)
                elif i.roozlist ==  "17-all": 
                    r2.remove(17)    
                elif i.roozlist ==  "18-all": 
                    r2.remove(18)    
                elif i.roozlist ==  "19-all": 
                    r2.remove(19)
                elif i.roozlist ==  "20-all": 
                    r2.remove(20)
                elif i.roozlist ==  "21-all": 
                    r2.remove(21)    
                elif i.roozlist ==  "22-all": 
                    r2.remove(22)    
                elif i.roozlist ==  "23-all": 
                    r2.remove(23) 
                elif i.roozlist ==  "24-all": 
                    r2.remove(24)    
                elif i.roozlist ==  "25-all": 
                    r2.remove(25)    
                elif i.roozlist ==  "26-all": 
                    r2.remove(26)
                elif i.roozlist ==  "27-all": 
                    r2.remove(27)
                elif i.roozlist ==  "28-all": 
                    r2.remove(28)    
                elif i.roozlist ==  "29-all": 
                    r2.remove(29)    
                elif i.roozlist ==  "30-all": 
                    r2.remove(30)    
                elif i.roozlist ==  "31-all": 
                    r2.remove(30)                                                        
              
                        
    return Response({'freeday': r2})


@api_view(['POST'])
def checkrooztime(request):
    d = datetime.datetime.now()
    mah = request.POST['mah']
    year = request.POST['year']
    daynow = int(datetime.datetime.today().day)
    rooz = request.POST['rooz']
    a = []
    r = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    rr = []
    bookdate = RezervModel.objects.filter(sallist=year, mahlist=mah, roozlist=rooz, Add_a_mot=True)
    for i in bookdate:
        if i.timelist == "08:00":
            rr.append("08:00")
        elif i.timelist == "09:00":
            rr.append("09:00")
        elif i.timelist == "10:00":
            rr.append("10:00")
        elif i.timelist == "11:00":
            rr.append("11:00")
        elif i.timelist == "12:00":
            rr.append("12:00")
        elif i.timelist == "13:00":
            rr.append("13:00")
        elif i.timelist == "14:00":
            rr.append("14:00")
        elif i.timelist == "15:00":
            rr.append("15:00")
        elif i.timelist == "16:00":
            rr.append("16:00")
        elif i.timelist == "17:00":
            rr.append("17:00")

    temp3 = []
    for element in r:
        if element not in rr:
            temp3.append(element)
            
    all_checked=AdminCheckedTime.objects.all()    
    if len(all_checked) > 0:
        for i in all_checked:
            
            if int(i.sallist) == int(year) and int(i.mahlist) == int(mah) and int(i.roozlist) == int(rooz):
                if i.timelist == "08:00":
                    temp3.remove("08:00")
                if i.timelist == "09:00":
                    temp3.remove("09:00")                    
                if i.timelist == "10:00":
                    temp3.remove("10:00")                       
                if i.timelist == "11:00":
                    temp3.remove("11:00")
                if i.timelist == "12:00":
                    temp3.remove("12:00")                       
                if i.timelist == "13:00":
                    temp3.remove("13:00")     
                if i.timelist == "14:00":
                    temp3.remove("14:00")                       
                if i.timelist == "15:00":
                    temp3.remove("15:00")  
                if i.timelist == "16:00":
                    temp3.remove("16:00")                       
                if i.timelist == "17:00":
                    temp3.remove("17:00")                       
                    
                                                                      
            
    return Response({'freetime': temp3})


@api_view(['POST'])
def checkmounth_2(request):
    d = datetime.datetime.now()
    mounthnow = int(d.strftime("%m"))
    daynow = int(datetime.datetime.today().day)
    mounth = request.POST['mounth']
    year = request.POST['year']
    m1 = [1, 3, 5, 6, 7, 8, 10, 12]  # نماینده  ماه هایی  که 31 روز است
    m2 = [4, 9, 11]  # نماینده ماه هایی که 30 روز است

    a = []
    r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31]
    r2 = []
    if int(mounth) in m1:
        pass
    elif int(mounth) in m2:
        r.pop()
    else:
        r.pop()
        r.pop()
    r2 = r
    if mounthnow == int(mounth):
        r = r[daynow - 1:]
        r2 = r
    all_checked=AdminCheckedTime.objects.all()    
    if len(all_checked) > 0:
        for i in all_checked:
            if int(i.sallist) == int(year) and int(i.mahlist) == int(mounth):
               if "all" in  i.roozlist:   
                if i.roozlist ==  "1-all": 
                    r2.remove(1)  
                elif i.roozlist ==  "2-all": 
                    r2.remove(2)
                elif i.roozlist ==  "3-all": 
                    r2.remove(3)
                elif i.roozlist ==  "4-all": 
                    r2.remove(4)
                elif i.roozlist ==  "5-all": 
                    r2.remove(5)
                elif i.roozlist ==  "6-all": 
                    r2.remove(6)
                elif i.roozlist ==  "7-all": 
                    r2.remove(7)
                elif i.roozlist ==  "8-all": 
                    r2.remove(8)
                elif i.roozlist ==  "9-all": 
                    r2.remove(9)
                elif i.roozlist ==  "10-all": 
                    r2.remove(10)
                elif i.roozlist ==  "11-all": 
                    r2.remove(11)  
                elif i.roozlist ==  "12-all": 
                    r2.remove(12)
                elif i.roozlist ==  "13-all": 
                    r2.remove(13)    
                elif i.roozlist ==  "14-all": 
                    r2.remove(14)    
                elif i.roozlist ==  "15-all": 
                    r2.remove(15)                      
                elif i.roozlist ==  "16-all": 
                    r2.remove(16)
                elif i.roozlist ==  "17-all": 
                    r2.remove(17)    
                elif i.roozlist ==  "18-all": 
                    r2.remove(18)    
                elif i.roozlist ==  "19-all": 
                    r2.remove(19)
                elif i.roozlist ==  "20-all": 
                    r2.remove(20)
                elif i.roozlist ==  "21-all": 
                    r2.remove(21)    
                elif i.roozlist ==  "22-all": 
                    r2.remove(22)    
                elif i.roozlist ==  "23-all": 
                    r2.remove(23) 
                elif i.roozlist ==  "24-all": 
                    r2.remove(24)    
                elif i.roozlist ==  "25-all": 
                    r2.remove(25)    
                elif i.roozlist ==  "26-all": 
                    r2.remove(26)
                elif i.roozlist ==  "27-all": 
                    r2.remove(27)
                elif i.roozlist ==  "28-all": 
                    r2.remove(28)    
                elif i.roozlist ==  "29-all": 
                    r2.remove(29)    
                elif i.roozlist ==  "30-all": 
                    r2.remove(30)    
                elif i.roozlist ==  "31-all": 
                    r2.remove(30)
    return Response({'freeday': r2})


@api_view(['POST'])
def checkrooztime_2(request):
    d = datetime.datetime.now()
    mah = request.POST['mah']
    year = request.POST['year']
    daynow = int(datetime.datetime.today().day)
    rooz = request.POST['rooz']
    a = []
    r = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    all_checked=AdminCheckedTime.objects.all()    
    if len(all_checked) > 0:
        for i in all_checked:
            
            if int(i.sallist) == int(year) and int(i.mahlist) == int(mah) and int(i.roozlist) == int(rooz):
                if i.timelist == "08:00":
                    r.remove("08:00")
                if i.timelist == "09:00":
                    r.remove("09:00")                    
                if i.timelist == "10:00":
                    r.remove("10:00")                       
                if i.timelist == "11:00":
                    r.remove("11:00")
                if i.timelist == "12:00":
                    r.remove("12:00")                       
                if i.timelist == "13:00":
                    r.remove("13:00")     
                if i.timelist == "14:00":
                    r.remove("14:00")                       
                if i.timelist == "15:00":
                    r.remove("15:00")  
                if i.timelist == "16:00":
                    r.remove("16:00")                       
                if i.timelist == "17:00":
                    r.remove("17:00") 
    return Response({'freetime': r})
