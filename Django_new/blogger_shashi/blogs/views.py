from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

names = ['Shashi', 'Bhushan', 'Bhagat']


def index(request):
    return HttpResponse("This is your first respose Shashi 🎃")


def getAllNames(request):
    return HttpResponse(names)


def add_names(request, value):
    global names
    names.append(value)

    return HttpResponse("\n".join(names))
