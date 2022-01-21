from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .models import Profile

# Image Validation
from django.core.files.images import get_image_dimensions

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

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        try:
            w, h = get_image_dimensions(avatar)
            print(avatar, w, h)
            #validate dimensions
            max_width = max_height = 1000
            min_width = min_height = 400
            if w > max_width or h > max_height:
                raise forms.ValidationError(u'Please use an image that is ''%s x %s pixels or smaller.' % (max_width, max_height))
            
            if w < min_width or h < min_height:
                raise forms.ValidationError(u'Please use an image that is at least ''%s x %s pixels.' % (min_width, min_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, or PNG image.')

            #validate file size
            if len(avatar) > (500 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 500Kb.')

        except AttributeError:
            pass

        return avatar