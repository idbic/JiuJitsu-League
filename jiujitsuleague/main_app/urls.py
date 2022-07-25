from django.urls import path
from . import views
from django.contrib import admin
from main_app.views import front



urlpatterns = [
path('admin/', admin.site.urls),
path("", front, name="front"),
path('', views.home, name='home'),
path('tournaments/', views.tournaments, name='tournaments'),
path('profile/', views.profile, name='profile'), 
path('login/', views.login, name='login'),
path('signup/', views.signup, name='signup'),
path('rankings/', views.rankings, name='rankings')
]