from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

#LOGIN
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            print(user)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
                #return HttpResponse("Konto zalogowane")
            else:
                return HttpResponse("Konto nie istnieje")
    else:
        form = LoginForm()
        return render (request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

#WEBSITE
def home(request):
    return render(request,"dashboard.html")