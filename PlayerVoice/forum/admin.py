from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Post, Like, Comment

class PostAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'title', 'description', 'author', 'created_at')
    search_fields = ('id', 'author__id')
    autocomplete_fields = ('author', )

class LikeAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'post', 'author')
    search_fields = ('id', 'author__id')
    autocomplete_fields = ('author', )

class CommentAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'comment', 'post', 'author', 'created_at')
    search_fields = ('id', 'post__id', 'author__id')
    autocomplete_fields = ('post', 'author', )


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)