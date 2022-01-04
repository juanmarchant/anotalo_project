from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.utils.translation import gettext_lazy as _

from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields =("username", "email", "password1", "password2")

    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The email is already registered, try another")
        return email

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar', 'background']
        widgets = {
            'avatar' : forms.ClearableFileInput(attrs={'class':'form-control mb-3'}),
            'background': forms.ClearableFileInput(attrs={'class':'form-control mb-3'})
        }