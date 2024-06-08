from django import forms
from .models import carModel

class ModelForm(forms.ModelForm):
    class Meta:
        model = carModel
        fields = '__all__'