from rest_framework import serializers
from .models import Bots
from django.contrib.auth.models import User

class BotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bots
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'