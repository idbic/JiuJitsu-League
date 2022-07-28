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
  tournament = Tournament.objects.get(id=tournament_id)
  return render(request, 'tournaments/detail.html', { 'tournament': tournament })


def profile(request): 
    return render(request, "profile.html")

def login(request): 
    return render(request, "login.html")

def signup(request): 
    return render(request, "signup.html")

def rankings(request):
    return render(request, "rankings.html")



from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.
  
class ReactView(APIView):
    
    serializer_class = ReactSerializer
  
    def get(self, request):
        detail = [ {"city": detail.city,"date": detail.date, "address": detail.address, "price": detail.price
        "user": detail.user} 
        for detail in React.objects.all()]
        return Response(detail)
  
    def post(self, request):
  
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)