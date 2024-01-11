from django.contrib import admin

from .models import CarModel


@admin.register(CarModel)
class CarAdmin(admin.ModelAdmin):
    list_display = ['tag', 'postal_code']
