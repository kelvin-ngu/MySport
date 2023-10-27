from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import MentalHealth, SelfRating
# from .serializers

# Create your views here.
# class PlayerViewSet(ModelViewSet):
#     queryset = Player.objects.all()
#     pagination_class = None

#     def retrieve(self, request, *args, **kwargs):
#         player = self.get_object()
#         data = 
#         return Response(player)