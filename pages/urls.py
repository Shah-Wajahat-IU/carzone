from unicodedata import name
from pages.views import home
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('service',views.contact,name='service'),
]