from django.utils import timezone
from rest_framework import serializers

from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    username = serializers.CharField()
    birth_year = serializers.DateField()
    club = serializers.CharField()
    role = serializers.CharField()

    class Meta:
        model = Player
        fields = '__all__'

class CreatePlayerSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    birth_year = serializers.DateField()
    club = serializers.CharField()
    role = serializers.CharField()

    class Meta:
        model = Player
        fields = '__all__'