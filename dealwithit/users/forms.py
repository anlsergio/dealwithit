from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # define the new property and its rules

    class Meta:
        model = User # model to be affected
        fields = [ # fields you want to be displayed
            'username',
            'email',
            'password1',
            'password2'
        ]