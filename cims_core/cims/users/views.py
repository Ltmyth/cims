from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# flash messages
from django.contrib import messages
# user database
from django.contrib.auth.models import User
# authenticate
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def index(request):
    return render(request, 'users/user_login.html')

def home(request):
    return render(request, 'users/index.html')

def about(request):
    return render(request, 'users/about.html')

#loging
def login(request):
    return render(request, 'users/user_login.html')

def login_user(request):
    user_name = request.POST['username']
    user_password = request.POST['password']
    if User.objects.filter(username = user_name).first():
        print("This username exists")
        user = authenticate(request, username=user_name, password=user_password)
        if user is not None:
            # login
            auth_login(request,user)
            messages.success(request, 'Login Success')
            #redirect
            return redirect('/home')
        else:
            # No authenticated the credentials
            messages.error(request, 'Wrong Username or Password.')
            return render(request, 'users/user_login.html')
    else:
        messages.success(request, 'Account created.')
        return render(request, 'users/user_login.html')

@login_required
def logout_user(request):
    auth_logout(request)
    messages.success(request, 'You have logged out. Bye!')
    return redirect('/login')

def create_user(request):
    user_name = request.POST['username']
    user_password = request.POST['password']
    user_email = request.POST['email']
    if User.objects.filter(username = user_name).first():
        messages.info(request, 'Account already exists')
        return render(request, 'users/user_create.html')
    else:
        messages.success(request, 'Account created.')
        user = User.objects.create_user(user_name, user_email, user_password)
        # Redirect to a success page.
        return render(request, 'users/user_login.html')

def create_user_page(request):
    # Redirect to a success page.
    return render(request, 'users/user_create.html')



def services(request):
    return render(request, 'users/services.html')

def team(request):
    return render(request, 'users/team.html')