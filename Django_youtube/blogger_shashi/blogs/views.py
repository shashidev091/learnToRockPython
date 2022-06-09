from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'index.html')

def about_page(request):
    return HttpResponse('Hi! I am Shashi Bhushan Bhagat')

def services_page(request):
    return HttpResponse('<b>We have several sevices, you just have to ask what</b>')