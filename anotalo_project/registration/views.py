from django.views.generic import CreateView
from django.views.generic.edit import  UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Forms
from .forms import UserCreationFormWithEmail, ProfileForm
from django import forms

# Redirect
from django.urls import reverse_lazy

# Models
from .models import Profile

# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
    
        # Inputs
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mt-2'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mt-2'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mt-2'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mt-2 mb-4'})

        # help text
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = "Use at least one letter, one numeral, and 8 characters."
        form.fields['password2'].help_text = None

        return form

method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('register:profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created =  Profile.objects.get_or_create(user = self.request.user)
        return profile

