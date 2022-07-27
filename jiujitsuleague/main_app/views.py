from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
# Home View

def front(request):
    context = { }
    return render(request, "index.html", context)

def home(request): 
    return render(request, 'home.html')

def tournaments(request): 
    return render(request, 'tournaments.html')


def tournaments_detail(request, tournament_id):
  tournament = Tournamentk.objects.get(id=tournament_id)
  return render(request, 'tournaments/detail.html', { 'tournament': tournament })


def profile(request): 
    return render(request, "profile.html")

def login(request): 
    return render(request, "login.html")

def signup(request): 
    return render(request, "signup.html")

def rankings(request):
    return render(request, "rankings.html")