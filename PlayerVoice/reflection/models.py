from uuid import uuid4
# from simple_history.models import HistoricalRecords

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from simple_history.models import HistoricalRecords

from player.models import Player

# Create your models here.
class MentalHealth(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    player = models.ForeignKey(Player,
                               null=True, blank=True,
                               on_delete=models.CASCADE,
                               related_name='mental_health_by_player')
    history = HistoricalRecords()

    class Meta:
        ordering = ['player']


class SelfRating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    player = models.ForeignKey(Player,
                               null=True, blank=True,
                               on_delete=models.CASCADE,
                               related_name='self_rating_by_player')
    rating = models.IntegerField(default=1,
                                 validators=[MaxValueValidator(10),
                                             MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ['player']