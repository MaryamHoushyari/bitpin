from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostScore(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='scores')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
    score = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.score} for {self.post}'
