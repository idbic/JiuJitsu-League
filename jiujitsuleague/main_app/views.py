from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
# Home View

def home(request): 
    return render(request, 'home.html')

def tournaments(request): 
    return render(request, 'tournaments.html')

def profile(request): 
    return render(request, "profile.html")

def login(request): 
    return render(request, "login.html")

def signup(request): 
    return render(request, "signup.html")

def rankings(request):
    return render(request, "rankings.html")