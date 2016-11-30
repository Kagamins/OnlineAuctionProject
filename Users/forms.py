from django import forms
from .models import *

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
            Phone_num= self.cleaned_data.get('Phone_num')
        )
class Message_Form(forms.ModelForm):
    class Meta:
        model = message
        fields = '__all__'
        widgets = {
        'sender' : forms.HiddenInput,
        'date_time_sent' : forms.HiddenInput,
        }
