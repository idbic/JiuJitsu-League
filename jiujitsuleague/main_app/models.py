from django.db import models

# Create your models here.
class Tournaments(models.model):
    city = models.Charfield(max_length=100, null=True)
    date = models.Charfield()