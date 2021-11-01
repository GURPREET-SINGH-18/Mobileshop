from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import shopcart

# Create your views here.


def index(request):
    sp=shopcart.objects.all()
    return render(request, 'index.html',{'shop':sp})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'login successfully')
            return redirect('/')
        else:
            messages.info(request, 'Invalid username and password')
            return render(request,"signup.html")
    else:
        messages.info(request, 'Please login First')
        return render(request,'login.html')


def signup(request):
        if request.method == 'POST':
            username = request.POST['username']
            first = request.POST['first']
            lastname = request.POST['lastname']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username=username, first_name=first, last_name=lastname, password=password,
                                        email=email)
            user.save()
            messages.success(request, "signup successfully")
            return redirect("/login")
        else:
            return render(request, 'signup.html')

def learnmore(request,myid):
    if request.user.is_authenticated:
        sp=shopcart.objects.filter(id=myid)
        print(sp)
        return render(request, "info.html", {'shop':sp[0]})
        #return render(request, 'info.html',{'shop':sp})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'logout successfully')
    return redirect("/")
        