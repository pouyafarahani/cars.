from django.db import models
from django.urls import reverse


class RezervModel(models.Model):

    Full_service = models.BooleanField(default=False)
    Interim_service = models.BooleanField(default=False)
    Add_a_mot = models.BooleanField(default=False)

    Wheelaligment = models.BooleanField(default=False)
    Diagnose = models.BooleanField(default=False)
    Tyres = models.BooleanField(default=False)
    Clutches = models.BooleanField(default=False)
    Suspension = models.BooleanField(default=False)
    Cambelt = models.BooleanField(default=False)
    Exhaust = models.BooleanField(default=False)
    Brakes = models.BooleanField(default=False)
    Batteries = models.BooleanField(default=False)

    
    other = models.TextField(null=True, blank=True)

    
    Firstname = models.CharField(max_length=80, verbose_name='Firts name')
    Lastname = models.CharField(max_length=80, verbose_name='last name')
    PhoneNumber = models.CharField(max_length=30, verbose_name='phone number')
    Email = models.EmailField(max_length=254, null=True, blank=True)
    Anything = models.TextField(null=True, blank=True)

    
    make = models.CharField(max_length=10, null=True, blank=True)
    register = models.CharField(max_length=20, null=True, blank=True)

    
    delivery = models.BooleanField(default=False)

    
    fixed = models.BooleanField(default=False)

    sallist = models.CharField(max_length=4, null=True, verbose_name='Years')
    mahlist = models.CharField(max_length=20, null=True, verbose_name='month')
    roozlist = models.CharField(max_length=20, null=True, verbose_name='Day')
    timelist = models.CharField(max_length=40, null=True, verbose_name='time')

    

    def __str__(self):
        return self.Lastname
        
    class Meta:
        verbose_name = 'Reserve'
        verbose_name_plural = 'Reserve'

    def get_absolute_url(self):
        return reverse('pages:factor', args=[self.pk])


class AdminCheckedTime(models.Model):
    sallist = models.CharField(max_length=8, null=True, verbose_name='Years')
    mahlist = models.CharField(max_length=24, null=True, verbose_name='month',blank=True)
    roozlist = models.CharField(max_length=24, null=True, verbose_name='Day',blank=True)
    timelist = models.CharField(max_length=44, null=True, verbose_name='time',blank=True)

    def __str__(self):
        return f'{self.sallist}/{self.mahlist}/{self.roozlist}'
    