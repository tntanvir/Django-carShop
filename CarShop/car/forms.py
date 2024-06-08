from django import forms
from .models import Car,CarComment

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude=['author']

class CarCommentForm(forms.ModelForm):
    class Meta:
        model = CarComment
        fields=['name', 'comment']