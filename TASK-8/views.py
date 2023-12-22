# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    # Add your login logic here
    return render(request, 'login.html')

def signup_view(request):
    # Add your signup logic here
    return render(request, 'signup.html')

def student_database_view(request):
    # Add your student database logic here
    return render(request, 'student_database.html')

def signout_view(request):
    # Add your signout logic here
    return render(request, 'signout.html')
