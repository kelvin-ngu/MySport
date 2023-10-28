from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Reflection
# from .serializers

class ReflectionViewSet(ModelViewSet):
    queryset = Reflection.objects.all()
    pagination_class = None

    def retrieve(self, request, *args, **kwargs):
        player = self.get_object()
        return Response(player)