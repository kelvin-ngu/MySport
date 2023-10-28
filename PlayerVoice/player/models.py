from uuid import uuid4
from simple_history.models import HistoricalRecords

from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords


# striker, goalkeeper, defender, 
# goals, tackles, saves, goals in target
class PlayerRole(models.TextChoices):
    STRIKER = 'STRIKER', _('STRIKER')
    GOALKEEPER = 'GOALKEEPER', _('GOALKEEPER')
    DEFENDER = 'DEFENDER', _('DEFENDER')


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('username', 'WEBMASTER')
        return self.create_user(email, password, **extra_fields)
    
class Player(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=20, unique=True)
    birth_year = models.IntegerField(null=True, blank=True)
    club = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=15,
                            choices=PlayerRole.choices,
                            null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ['username']