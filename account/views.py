from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . models import Account
from django.contrib import messages


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:dashboard')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login')

    return render(request, 'login.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username already exists!')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'This is email address is already exists!')
            return redirect('signup')
        if password != confirm_password:
            messages.error(request, 'Password does not match')
            return redirect('signup')
        
        creat_user = User.objects.create_user(username=username, email=email, password=password)
        creat_user.save()
        
        return redirect('login')
    
    return render(request, 'signup.html')


def log_out(request):
    logout(request)
    return redirect('login')