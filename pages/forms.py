from django import forms

from .models import CarModel


class CarForms(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
