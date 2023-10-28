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

from reflection.views import is_content_safe

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
        if not is_content_safe(request.data.get('title')) or not is_content_safe(request.data.get('description')):
            return Response({
                'error': 'This is a friendly community, please edit your content'
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['POST'])
    def comment(self, request, *args, **kwargs):
        post = self.get_object()
        if not is_content_safe(request.data.get('comment')):
            return Response({
                'error': 'This is a friendly community, please edit your content'
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = CreateCommentSerializer(data={
            'comment': request.data.get('comment'),
            'post': post.id,
            'author': request.data.get('author'),
        })
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['POST'])
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = CreateLikeSerializer(data={
            'post': post.id,
            'author': request.data.get('author')
        })
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)