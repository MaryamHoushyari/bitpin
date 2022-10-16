from django.contrib import admin

from post.models import Post


@admin.register(Post)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    search_fields = ('title', 'body', 'author__username')
    list_filter = ('created', 'author__username')
