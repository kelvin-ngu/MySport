from uuid import uuid4
# from simple_history.models import HistoricalRecords

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from simple_history.models import HistoricalRecords

from player.models import Player

class Reflection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    player = models.ForeignKey(Player,
                               null=True, blank=True,
                               on_delete=models.CASCADE,
                               related_name='reflection_by_player')
    # match_description = models.TextField(required=True)
    rating = models.IntegerField(default=1,
                                 validators=[MaxValueValidator(10),
                                             MinValueValidator(1)])
        