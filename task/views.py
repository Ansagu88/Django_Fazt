
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})

    else:
        if request.POST ['password1'] == request.POST['password2']:
            # Create the User
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error':'User already exists'
                    })
        return render(request, 'signup.html', {
            'form': UserCreationForm(),
            'error':'Password did not match'
            })

def tasks(request):
    return render(request, 'tasks.html')

def signout(request):
    logout(request)
    return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('tasks')