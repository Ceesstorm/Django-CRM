from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in, please try again.")
            return render(request, 'home.html', {})  # Return the response even after failed login
    else:
        return render(request, 'home.html', {})  # Handle GET request

def register_user(request):
    return render(request, 'register.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "yuo have been logged out...")
    return redirect('home')

