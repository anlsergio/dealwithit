from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def register(request):

    # Conditional logic to check if the current HTTP method is actually a POST method
    # So we can create an instance of the form with the data which is passing in by the POST method
    # In order to validate that data, because a POST data could carry pretty much anything, and we don't want that
    # Otherwise, a blank instance of the form is created, since it's probably a GET method (when we navigate to the register page for example)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # If the form has valid data when submited...
            form.save()
            username = form.cleaned_data.get('username') # The validated data will be accessible by the "cleaned_data" method
            messages.success(request, f'Welcome {username}! Your account has been created')
            return redirect('login')
    else:
        form = UserRegisterForm() # It makes use of a Django's pre backed form called UserCreationForm which is instantiated inside forms.py file
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')