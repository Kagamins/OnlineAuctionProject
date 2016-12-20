from django import forms
from .models import *


class Newticketform(forms.ModelForm):
    class Meta:
        model = ticket
        fields = '__all__'
        widgets = {
        'user' : forms.HiddenInput,
        }
