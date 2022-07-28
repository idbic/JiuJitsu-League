from rest_framework import serializers
from . models import *
  
class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['city', 'date', 'address', 'price', 'user']