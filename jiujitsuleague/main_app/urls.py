from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('tournaments/', views.tournaments, name='tournaments'),
path('profile/', views.profile, name='profile'), 
path('login/', views.login, name='login'),
path('signup/', views.signup, name='signup'),
path('rankings/', views.rankings, name='rankings')
]