from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('reflection', views.ReflectionViewSet, basename='reflection')
router.register('journal', views.JournalViewSet, basename='journal')

urlpatterns = [
    path('', include(router.urls)),
]