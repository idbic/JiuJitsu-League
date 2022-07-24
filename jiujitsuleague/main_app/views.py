from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Home View

def home(request): 
    return HttpResponse("hey it me Jiu jitsu League")

def tournaments(request): 
    return HttpResponse("Tournaments Page Jiu Jitsu League")

def profile(request): 
    return HttpResponse("Settings/ Profile information")

def login(request): 
    return HttpResponse("Login page")

def signup(request): 
    return HttpResponse("signup")