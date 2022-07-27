from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tournaments(models.Model):
    city = models.CharField(max_length=100, null=True)
    date = models.DateField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    prices = models.CharField(max_length=100, null=True)
    athletes = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Athlete(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(max_length=100, null=True)
    weight = models.IntegerField(max_length=100, null=True)
    rank = models.CharField(max_length=100, null=True)
