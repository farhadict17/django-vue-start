from django.shortcuts import render
from django.http import HttpResponse
from .models import contact

# Create your views here.

def contactus(request):
    if request.method=='POST':
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # message = request.POST.get('message')

        #contactdata=contact(name=name,email=email,subject=subject,message=message)
        
        # or use like below
        contactdata = contact()
        contactdata.name=request.POST.get('name')
        contactdata.email=request.POST.get('email')
        contactdata.subject=request.POST.get('subject')
        contactdata.message=request.POST.get('message')
        contactdata.save()

    return render(request, 'contact.html')
    
    #return HttpResponse('This is contact page')
