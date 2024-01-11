from django.contrib import admin

from .models import RezervModel,AdminCheckedTime
# Register your models here.
# admin.site.register(RezervModel)


@admin.register(RezervModel)
class RezervAdmin(admin.ModelAdmin):
    list_display = ['Firstname', 'Lastname','mahlist','roozlist','timelist','Add_a_mot', 'PhoneNumber', 'make', 'fixed']


admin.site.register(AdminCheckedTime)