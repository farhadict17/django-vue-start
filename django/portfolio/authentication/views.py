from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def authlogin(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        print('name={} and password={}'.format(name,password))

        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            print("Welcome login Succeded")
            return redirect('employee.profile')

        else:  
            #print('invalid username of password')
            messages.error(request, 'Email or Password is wrong please try again!')  

    return render(request,'authentication/login.html')
    #return HttpResponse('This is Your login view')
def authregistraton(request):
    if request.method=='POST':
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exist')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exist')
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()
                messages.success(request, 'Sucessfully registration completed')
                return redirect('login')
        else:
            messages.error(request, 'Password and confirm_password does not match please check')  

    return render(request,'authentication/registration.html')

def forgotpassword(request):
    return render(request,'authentication/forgot.html')

def userlogout(request):
    logout(request)
    messages.success(request, 'Successfully Logout!')
    return redirect('login')