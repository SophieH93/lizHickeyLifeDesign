from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_liz, name='about_liz'),
]