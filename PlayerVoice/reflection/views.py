from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Reflection, Journal
from .serializers import (
    ReflectionSerializer, CreateReflectionSerializer,
    JournalSerializer, CreateJournalSerializer
)

class ReflectionViewSet(ModelViewSet):
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer
    pagination_class = None

    def retrieve(self, request, *args, **kwargs):
        reflection = self.get_object()
        serializer = ReflectionSerializer(reflection)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def list(self, request, *args, **kwargs):
        reflections = self.get_queryset()
        serializer = ReflectionSerializer(reflections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = CreateReflectionSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class JournalViewSet(ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    pagination_class = None
    
    def retrieve(self, request, *args, **kwargs):
        journal = self.get_object()
        serializer = JournalSerializer(journal)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def list(self, request, *args, **kwargs):
        journals = self.get_queryset()
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = CreateJournalSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)