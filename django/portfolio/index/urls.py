from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
   # path('profile/', views.profile,name='profile'),
    path('about/',views.aboutus,name='about'),
    path('team/',views.team,name='team'),
    path('services/',views.services,name='services'),
    #path('contact/',views.contactus,name='contact'),
]