from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    # return HttpResponse("Hello Shashi 😍")
    a = 20
    b = 30
    return render(request, 'hello.html', {'name': "Shashi"})