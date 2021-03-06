from django import forms
from .models import *
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
        'user' : forms.HiddenInput,


        }
    # university_id = forms.CharField(required=False)
    # twitter_id = forms.CharField(required=False)

    def signup(self, request, user):
        User.objects.create(
            user=user,
            name=user.username,
            email=user.email,
            Phone_number= self.cleaned_data.get('Phone_number')
        )

class Message_Form(forms.ModelForm):
    class Meta:
        model = message
        fields = '__all__'
        widgets = {
        'sender' : forms.HiddenInput,
        'date_time_sent' : forms.HiddenInput,
        }

class Message_Form_Auction(forms.ModelForm):
    class Meta:
        model = message
        fields = '__all__'
        widgets = {
        'sender' : forms.HiddenInput,
        'receiver' : forms.HiddenInput,
        'date_time_sent' : forms.HiddenInput,
        }

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
                'Date_Of_Birth' : DateWidget(bootstrap_version=3),
                'user' : forms.HiddenInput,

        }
