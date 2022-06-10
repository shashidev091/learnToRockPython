from django import views
from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.landing_page, name='home'),
    path('about-us', views.about_page, name='about'),
    path('services', views.services_page, name='services'),
    path('blog', views.blog, name='blog')
]