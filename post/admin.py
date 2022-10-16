from django.contrib import admin

from post.models import Post, PostScore


@admin.register(Post)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    search_fields = ('title', 'body', 'author__username')
    list_filter = ('author__username', 'created', 'modified')


@admin.register(PostScore)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'score', 'created')
    search_fields = ('post__title', 'score', 'author__username')
    list_filter = ('post__title', 'score', 'author__username', 'created', 'modified')
    list_editable = ('score', )
