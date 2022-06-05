from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_page),
    path('blog', views.index),
    path('get_names', views.getAllNames),
    path('<int:value>', views.redirect_to_facebook),
    path('<str:value>', views.add_names),
]