from django import forms

from.models import Residente

class ResidenteForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields= '__all__'
        
        