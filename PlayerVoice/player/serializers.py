from django.utils import timezone
from rest_framework import serializers

from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    age = serializers.IntegerField()
    club = serializers.CharField()

    class Meta:
        model = Player