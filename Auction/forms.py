from django import forms
from django.forms.models import inlineformset_factory
from .models import *
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

class newAuctionForm(forms.ModelForm):
    class Meta:
        model = auction
        fields = '__all__'
        widgets  = {'user' : forms.HiddenInput,



        }

class newLiveAuctionForm(forms.ModelForm):
    class Meta:
        model = live_auction
        exclude = ['winining_bid','auction_winner',]
        widgets  = {'owner' : forms.HiddenInput,
        }

class EditAuctionForm(forms.ModelForm):
    class Meta:
        model = auction
        exclude = ['product']
        widgets = {'user' : forms.HiddenInput}

class newProductForm(forms.ModelForm):
    class Meta:
        model = item
        fields = '__all__'
        widgets = {
        'owner' : forms.HiddenInput,
        'picture' : forms.ClearableFileInput()}

class newBidForm(forms.ModelForm):
    class Meta:
        model = bid
        fields = '__all__'
        widgets  = {'Bidder' : forms.HiddenInput,
                        'l_auction': forms.HiddenInput,}

class UpdateBidForm(forms.ModelForm):
    class Meta:
        model = bid
        fields = '__all__'
        widgets  = {'Bidder' : forms.HiddenInput,
                    'l_auction':forms.HiddenInput,}

class newPictureUpload(forms.ModelForm):
    class Meta:
        model = Picture
        fields = '__all__'
        widgets = {'user': forms.HiddenInput,}

class newPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {'User' : forms.HiddenInput}
