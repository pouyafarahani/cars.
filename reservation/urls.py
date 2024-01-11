from django.urls import path

from django.views.generic import TemplateView
from .views import RezervView

app_name = 'reservations'


urlpatterns = [
    path('', RezervView, name='rezerv'),
    path('contact/', TemplateView.as_view(template_name='pages/contact.html'), name='contact'),
]
