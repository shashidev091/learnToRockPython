from django.http import HttpResponse
from django.shortcuts import render

personal_info = {
    "name": "Shashi Bhagat",
    "mobile_no": "9931920057"
}
# Create your views here.


def landing_page(request):
    return render(request, 'index.html')


def about_page(request):
    # return HttpResponse('Hi! I am Shashi Bhushan Bhagat')
    return render(request, 'aboutUs.html', personal_info)


def services_page(request):
    return HttpResponse('<b>We have several sevices, you just have to ask what</b>')


def blog(request):
    return render(request, 'blog.html')
