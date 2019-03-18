from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .models import Profile


# This is where you can define your own custom form to include in the view
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Define the new property and its rules
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'light',
            }
        )
    )

    class Meta:
        model = User # Model to be affected
        fields = [ # Fields you want to be displayed
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

class ProfileUpdateForm(forms.ModelForm):
    phone_number = PhoneNumberField(label='Phone Number (+9999999999 up to 15 digits)')
    phone_number_is_public = forms.BooleanField(label="Show my phone number", required=False)
    class Meta:
        model = Profile
        fields = [
            'image',
            'phone_number',
            'phone_number_is_public',
            'city',
            'state'
        ]