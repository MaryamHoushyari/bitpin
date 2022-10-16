from rest_framework import viewsets

from post.models import Post, PostScore
from post.serializers import PostSerializer, PostScoreSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostScoreViewSet(viewsets.ModelViewSet):
    queryset = PostScore.objects.all()
    serializer_class = PostScoreSerializer
