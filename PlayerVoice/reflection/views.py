from nltk.sentiment.vader import SentimentIntensityAnalyzer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Reflection, Journal
from .serializers import (
    ReflectionSerializer, CreateReflectionSerializer,
    JournalSerializer, CreateJournalSerializer
)


def is_content_safe(content):
    sia = SentimentIntensityAnalyzer()
    threshold = 0.4
    return sia.polarity_scores(content)['neg'] < threshold

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
        print(request.data)
        # if not is_content_safe(request.data.get('title')) or not is_content_safe(request.data.get('entry')):
        #     return Response({
        #         'error': 'This is a friendly community, please edit your content'
        #     }, status=status.HTTP_400_BAD_REQUEST)
        serializer = CreateJournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)