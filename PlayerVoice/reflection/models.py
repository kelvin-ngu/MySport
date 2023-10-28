from uuid import uuid4
from datetime import datetime

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
    rating = models.IntegerField(default=1,
                                 validators=[MaxValueValidator(10),
                                             MinValueValidator(1)])
    match_description = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['player', 'created_at']


class Journal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    player = models.ForeignKey(Player,
                               null=True, blank=True,
                               on_delete=models.CASCADE,
                               related_name='journal_by_player')
    public = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['player', 'created_at']

    ## TODO: 
    # reflection models, viewsets
    # moderation package
    # authorisation, login