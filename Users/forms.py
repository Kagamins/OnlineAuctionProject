from django import forms
from .models import User
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
        Student.objects.create(
            user=user,
            name=user.username,
            email=user.email,
            twitter_id=self.cleaned_data.get('twitter_id')
        )
