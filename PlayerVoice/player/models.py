from uuid import uuid4
from simple_history.models import HistoricalRecords

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords


# striker, goalkeeper, defender, 
# goals, tackles, saves, goals in target
class PlayerRole(models.TextChoices):
    STRIKER = 'STRIKER', _('STRIKER')
    GOALKEEPER = 'GOALKEEPER', _('GOALKEEPER')
    DEFENDER = 'DEFENDER', _('DEFENDER')


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=20, default=None, null=True)
    birth_year = models.DateField()
    club = models.CharField(max_length=50)
    role = models.CharField(max_length=15,
                            choices=PlayerRole.choices,
                            null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ['club']