from rest_framework import serializers

from post.models import Post, PostScore


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostScore
        fields = '__all__'
