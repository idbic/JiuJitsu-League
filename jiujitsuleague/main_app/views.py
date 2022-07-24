from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
# Home View

def home(request): 
    return HttpResponse("hey it me Jiu jitsu League")

def tournaments(request): 
    return render(request, 'tournaments.html')

def profile(request): 
    return HttpResponse("Settings/ Profile information")

def login(request): 
    return HttpResponse("Login page")

def signup(request): 
    return HttpResponse("signup")