from django.http import HttpResponse
from django.shortcuts import render
#from django.template.response import TemplateResponse
from . models import about
from . models import slider
from . models import client

def home (request):
    #aboutdata=about.objects.all()
    aboutdata=about.objects.all()[0]
    sliderdata=slider.objects.all()
    clientdata=client.objects.all()
    context = {
        'about':aboutdata,
        'slider':sliderdata,
        'clients':clientdata,
    }
    
    return render(request,'index.html',context)

def aboutus (request):
    
    return render(request,'about.html')

def team (request):
    return render(request,'team.html')
   #return HttpResponse("This is  our team page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is our service pages")

#def contactus (request):
    #return render(request,'contact.html')