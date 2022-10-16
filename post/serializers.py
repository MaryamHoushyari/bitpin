from rest_framework import serializers

from post.models import Post, PostScore


class PostSerializer(serializers.ModelSerializer):
    score_average = serializers.CharField(read_only=True)
    no_score_users = serializers.CharField(read_only=True)
    your_score = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_your_score(self, obj):
        user = self.context['request'].user
        if not user.is_anonymous:
            scored = obj.scores.filter(author=user)
            return scored.first().score if scored else None


class PostScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostScore
        fields = '__all__'
