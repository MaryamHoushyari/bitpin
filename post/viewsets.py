from rest_framework import viewsets

from post.models import Post, PostScore
from post.serializers import PostSerializer, PostScoreSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostScoreViewSet(viewsets.ModelViewSet):
    queryset = PostScore.objects.all()
    serializer_class = PostScoreSerializer
