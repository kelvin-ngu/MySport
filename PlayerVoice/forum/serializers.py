# from profanity_check import predict

from rest_framework import serializers

from .models import Post, Like, Comment
from player.models import Player
from player.serializers import PlayerSerializer

class PostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    description = serializers.CharField()
    author = PlayerSerializer()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Post
        fields = '__all__'

class CreatePostSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())

    # def validate_description(self, value):
    #     if not is_content_safe(value):
    #         raise serializers.ValidationError("Remember we are a friendly community, please edit your content")
    #     return value

    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    like = serializers.CharField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    author = PlayerSerializer()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Like
        fields = '__all__'

class CreateLikeSerializer(serializers.ModelSerializer):
    like = serializers.CharField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    author = PlayerSerializer()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    comment = serializers.CharField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    author = PlayerSerializer()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Comment
        fields = '__all__'

class CreateCommentSerializer(serializers.ModelSerializer):
    comment = serializers.CharField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    author = PlayerSerializer()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Comment
        fields = '__all__'


# def is_content_safe(content):
#     threshold = 0.4
#     return predict([content]) < thrfrom django.utils import timezone
from rest_framework import serializers

from .models import Post, Like, Comment
from player.models import Player
from player.serializers import PlayerSerializer

class PostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    category = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    author = PlayerSerializer()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Post
        fields = '__all__'

class CreatePostSerializer(serializers.ModelSerializer):
    category = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())

    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    like = serializers.CharField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    author = PlayerSerializer()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Like
        fields = '__all__'

class CreateLikeSerializer(serializers.ModelSerializer):
    like = serializers.CharField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    author = PlayerSerializer()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    comment = serializers.CharField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    author = PlayerSerializer()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Comment
        fields = '__all__'

class CreateCommentSerializer(serializers.ModelSerializer):
    comment = serializers.CharField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    author = PlayerSerializer()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Comment
        fields = '__all__'