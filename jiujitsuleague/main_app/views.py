from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Home View

def home(request): 
    return HttpResponse("hey it me Jiu jitsu League")