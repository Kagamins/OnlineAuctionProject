from django import forms
from django.forms.models import inlineformset_factory
from .models import auction,item,bid
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

class newAuctionForm(forms.ModelForm):
    class Meta:
        model = auction
        fields = '__all__'
        dateTimeOptions = {
            'format': 'dd/mm/yyyy HH:ii P',
            'autoclose': True,
            'showMeridian': True
        }
        widgets  = {'user' : forms.HiddenInput,
                    'auction_date' : DateWidget(bootstrap_version=3),
                    'auction_time' : TimeWidget(bootstrap_version=3)


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
        widgets = { 'picture' : forms.ClearableFileInput()}

class newBidForm(forms.ModelForm):
    class Meta:
        model = bid
        fields = '__all__'
        widgets  = {'Bidder' : forms.HiddenInput}
    def newbid(self,request,user):
        bid.objects.create(
        Bidder = user,
        User_bid = self.cleaned_data.get('User_bid'),
        Time_of_Bid = self.cleaned_data.get('Time_of_Bid'),
        l_auction= self.cleaned_data.get('l_auction'))
