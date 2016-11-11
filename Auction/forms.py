from django import forms
from django.forms.models import inlineformset_factory
from .models import auction,item

class newAuctionForm(forms.ModelForm):
    class Meta:
        model = auction
        fields = '__all__'
        widgets  = {'user' : forms.HiddenInput

        }
