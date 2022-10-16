from rest_framework import viewsets

from post.models import Post, PostScore
from post.serializers import PostSerializer, PostScoreSerializer


class PostViewSet(viewsets.ModelViewSet):
    model = Post
    serializer_class = PostSerializer


class PostScoreViewSet(viewsets.ModelViewSet):
    model = PostScore
    serializer_class = PostScoreSerializer
