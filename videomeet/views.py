from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(request) :
    message = ''
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None :
            auth.login(request, user)
            return redirect('dashboard')
        else :
            message = "Username and Password doest Match"
            return render(request, "login.html", {'message': message})

    return render(request, "login.html", {'message': message})

def register_user(request) :
    message = ''
    if request.method == 'POST' :
        first_name = request.POST.get('first_name', False)
        last_name = request.POST['last_name']
        user_email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        register = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            email = user_email,
            username = username,
            password = password
        )
        register.save()
        return render(request, 'login.html', {})
        message = 'User Successfully Register'
    return render(request, 'register.html', {'message' : message})

@login_required
def dashboard(request) :
    return render(request, 'dashboard.html', {})

@login_required
def create_video(request) :
    return render(request, 'videocall.html', {})

@login_required
def join_video(request) :
    return render(request, 'videocall.html', {})

def logout_view(request) :
    logout(request)
    return redirect('/')


