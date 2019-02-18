from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse('<h1>Store home</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')