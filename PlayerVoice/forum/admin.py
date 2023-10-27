from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Journal

class JournalAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'title', 'description', 'author', 'created_at')
    search_fields = ('id', 'author__id')
    autocomplete_fields = ('author', )

admin.site.register(Journal, JournalAdmin)