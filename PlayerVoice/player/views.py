from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .models import Player
from .serializers import PlayerSerializer

# Create your views here.
class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    pagination_class = None

    def retrieve(self, request, *args, **kwargs):
        player = self.get_object()
        serializer_data = self.get_serializer()
        return Response(serializer_data, status=status.HTTP_200_OK)