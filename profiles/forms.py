from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms

from captcha.fields import ReCaptchaField

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captcha')
        field_classes = {'username': UsernameField}
        widgets = {
            'email': forms.EmailInput(attrs={'required': True})
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'address', 'year_birth', 'about')

