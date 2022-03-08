import parser

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Services, Team


def home(request):
    fetch_services = Services.objects.all()
    fetch_team = Team.objects.all()
    return render(request, 'index.html', {'result_services': fetch_services, 'result_team': fetch_team})


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password == re_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "user already exists")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email,
                                                password=password)
                user.save()
                print('user created')
        else:
            messages.info(request, "passwords does not match")
            return redirect('signup')

        return redirect('login')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('user logged in')
            redirect('/')
        else:
            messages.info(request, "invalid login credentials")
            redirect('login')
        return redirect('/')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
