from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home-page'),
    path('about/', views.aboutView, name='about-page'),
    path('contact/', views.contactView, name='contact-page'),
]


