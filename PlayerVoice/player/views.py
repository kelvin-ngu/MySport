from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .models import Player
from .serializers import PlayerSerializer, CreatePlayerSerializer

# Create your views here.
class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    pagination_class = None

    def retrieve(self, request, *args, **kwargs):
        player = self.get_object()
        serializer = player.get_serializer()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def list(self, request, *args, **kwargs):
        players = self.get_queryset()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = CreatePlayerSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)