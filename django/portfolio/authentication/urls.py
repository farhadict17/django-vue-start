from django.urls import path
from . import views

urlpatterns = [
    path('',views.authlogin,name='login'), 
    path('registraton/',views.authregistraton,name='registraton'),
    path('forgot-password/',views.forgotpassword,name='forgotpassword'), 
    path('logout/',views.userlogout,name='logout'), 
]