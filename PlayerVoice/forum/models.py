from uuid import uuid4
from simple_history.models import HistoricalRecords

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords

from player.models import Player

# Create your models here.

class Category(models.TextChoices):
    PHYSICAL_CARE = 'PHYSICAL_CARE', _('PHYSICAL_CARE')
    MENTAL_HEALTH = 'MENTAL_HEALTH', _('MENTAL_HEALTH')
    PLAYER_VOICE = 'PLAYER_VOICE', _('PLAYER_VOICE')
    PHYSICAL_PERFORMANCE = 'PHYSICAL_PERFORMANCE', _('PHYSICAL_PERFORMANCE')


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category = models.CharField(max_length=50,
                                choices=Category.choices,
                                null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Player,
                               null=True, blank=True,
                               on_delete=models.CASCADE,
                               related_name='post_by_player')
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ['created_at']

class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    post = models.ForeignKey(Post,
                                null=True, blank=True,
                                on_delete=models.CASCADE,
                                related_name='like_by_post')
    author = models.ForeignKey(Player,
                               null=True, blank=True,
                               on_delete=models.CASCADE,
                               related_name='like_by_player')
    history = HistoricalRecords()
    
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    comment = models.TextField()
    post = models.ForeignKey(Post,
                                null=True, blank=True,
                                on_delete=models.CASCADE,
                                related_name='comment_by_post')
    author = models.ForeignKey(Player,
                               null=True, blank=True,
                               on_delete=models.CASCADE,
                               related_name='comment_by_player')
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ['created_at']