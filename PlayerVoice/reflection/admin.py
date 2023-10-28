from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Journal, Reflection

class JournalAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'player', 'public', 'title', 'created_at')
    search_fields = ('id',)

class ReflectionAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'player', 'rating', 'match_description', 'comment', 'created_at')
    search_fields = ('id',)

admin.site.register(Journal, JournalAdmin)
admin.site.register(Reflection, ReflectionAdmin)