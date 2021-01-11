'''
from django.http import HttpResponse
from django.shortcuts import render
#from django.template.response import TemplateResponse


def home (request):
    text = {
        "name":"Farhad Ali",
        "age":30,
        "phone": 7028070332,
        "friend_name":["Riad","Sumon","Rizbi","Sourav","Shuvo"]
    }
    return render(request,'index.html',text) # render by default in template directory so no need to mention the template
    #return HttpResponse("This is  our home page")


def about (request):
    #data = "It will show all about related data from about table"
    return render(request,'about.html')
    #return HttpResponse(data)
    

def contact (request):
    return render(request,'contact.html')
    '''