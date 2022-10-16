from django.db import transaction
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

    def update(self, instance, validated_data):
        """
        I've written this method because you asked me to consider this as real production

        I think in real projects we may need to be able to create or update scores for a post in
        the same url as we can update the post!
        """
        with transaction.atomic():
            instance = super(PostSerializer, self).update(instance, validated_data)

            if "score" in self.initial_data:
                score = self.initial_data.get("score")
                score["post"] = instance.id
                score["author"] = self.context['request'].user
                old_score = PostScore.objects.filter(author=score["author"], post=score["post"])
                if old_score:
                    score_serializer = PostScoreSerializer(instance=old_score[0], data=score)
                else:
                    score_serializer = PostScoreSerializer(data=score)
                score_serializer.is_valid(raise_exception=True)
                score_serializer.save()

            return instance


class PostScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostScore
        fields = '__all__'
