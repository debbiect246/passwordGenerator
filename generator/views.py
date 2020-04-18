from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from generator import views


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    return render(request, 'generator/password.html')
