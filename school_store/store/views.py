from urllib import request

from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Store


# Create your views here.
def stores(request):
    return render(request, 'start.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('store_app:home')
        else:
            messages.info(request, 'invalid information')
            return redirect('store_app:login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('store_app:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('store_app:login')

        else:
            messages.info(request, 'password mismatch')
            return redirect('store_app:register')
        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age=request.POST.get('y')
        gender = request.POST.get('g')
        pnum = request.POST.get('ph')
        mail = request.POST.get('mail')
        address = request.POST.get('address')
        department = request.POST.get('dept')
        course = request.POST.get('cors')
        purpose = request.POST.get('purp')
        material = request.POST.getlist('mp')
        store = Store(name=name, dob=dob,age=age, gender=gender, ph=pnum, email=mail, address=address,
                      dept=department, course=course,
                      purpose=purpose, material=material)
        store.save()
        return redirect('store_app:submitt')

    return render(request, 'home.html',{"obj1":"commerce"})


def submitt(request):
    return render(request,'submitt.html')