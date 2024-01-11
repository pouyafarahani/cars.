from django import forms

from .models import RezervModel


class RezervForm(forms.ModelForm):
    class Meta:
        model = RezervModel
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(RezervForm, self).__init__(*args, **kwargs)
        self.fields['timelist'].required = False