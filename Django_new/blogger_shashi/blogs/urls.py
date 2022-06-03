from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.index),
    path('get_names', views.getAllNames),
    path('<str:value>', views.add_names)
]