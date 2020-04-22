from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
#from generator import views


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    # list of characters to chose from
    characters = list('abcdefghijklmnopqrstuvwxyz')

    # list of upper case characters to choose from
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # list of special characters to choose from
    if request.GET.get('special'):
        characters.extend(list('!£$%&*()@~'))

    # list of number character to choose from
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    # get user requested length, default is 12 characters
    length = int(request.GET.get('length', 12))

    thepassword = ''
    for bit in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
