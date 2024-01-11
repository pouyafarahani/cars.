from django.contrib import admin
from django.urls import path, include
from reservation.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('book/', include('reservation.urls')),
    path('checkyear', checkyear, name='checkyear'),
    path('checkmounth', checkmounth, name='checkmounth'),
    path('checkrooztime', checkrooztime, name='checkrooztime'),
    path('checkmounth_2', checkmounth_2, name='checkmounth_2'),
    path('checkrooztime_2', checkrooztime_2, name='checkrooztime_2'),

]
