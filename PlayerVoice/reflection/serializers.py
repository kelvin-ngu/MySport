from django.utils import timezone
from rest_framework import serializers

from .models import SelfRating, MentalHealth
from player.models import Player

class SelfRatingSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())

    class Meta:
        fields = '__all__'