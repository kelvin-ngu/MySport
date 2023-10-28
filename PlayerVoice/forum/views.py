from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .models import Post, Like, Comment
from .serializers import (
    PostSerializer, CreatePostSerializer,
    LikeSerializer, CreateLikeSerializer,
    CommentSerializer, CreateCommentSerializer
)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = None

    def retrieve(self, request, *args, **kwargs):
        post = self.get_object()
        like_amount = len(post.like_by_post.all())
        comments = post.comment_by_post.all()
        data = {
            'post': PostSerializer(post).data,
            'likes': like_amount,
            'comments': CommentSerializer(comments, many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def list(self, request, *args, **kwargs):
        posts = self.get_queryset()
        data = []
        for post in posts:
            like_amount = len(post.like_by_post.all())
            comments = post.comment_by_post.all()
            post_data = {
                'post': PostSerializer(post).data,
                'likes': like_amount,
                'comments': CommentSerializer(comments, many=True).data
            }
            data.append(post_data)
        return Response(data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = CreatePostSerializer(data=request.data)#{
            # 'category': request.data.get('category'),
            # 'title': request.data.get('title'),
            # 'description': request.data.get('description'),
            # 'author': request.data.get
        #})
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)