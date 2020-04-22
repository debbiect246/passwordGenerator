from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
#from generator import views


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for bit in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
