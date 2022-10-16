from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
