from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Define the new property and its rules

    class Meta:
        model = User # Model to be affected
        fields = [ # Fields you want to be displayed
            'username',
            'email',
            'password1',
            'password2'
        ]