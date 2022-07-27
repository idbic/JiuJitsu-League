from django.urls import path
from . import views
from django.contrib import admin




urlpatterns = [
path('admin/', admin.site.urls),
path("", views.front, name="front"), #this is the react url
# path('', views.home, name='home'),
path('tournaments/', views.tournaments, name='tournaments'),
path('tournaments/<int:tournaments_id>', views.tournaments_detail, name='detail'),
path('profile/', views.profile, name='profile'), 
path('login/', views.login, name='login'),
path('signup/', views.signup, name='signup'),
path('rankings/', views.rankings, name='rankings'),
path('accounts/', include('django.contrib.auth.urls')),
]