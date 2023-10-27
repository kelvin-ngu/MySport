from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Player

class PlayerAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'birth_year', 'role', 'club')
    search_fields = ('id',)

admin.site.register(Player, PlayerAdmin)