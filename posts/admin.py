from django.contrib import admin
from .models import PostModel, CommentModel
from bloggers.models import BloggerModel


class CommentAdmin(admin.StackedInline):
    model = CommentModel
    fields = ['post', 'author', 'text']
    extra = 0


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'blogger', 'likes_count', 'comment_count', ]
    list_filter = ['is_enable']
    search_fields = ['title']
    inlines = [CommentAdmin]


@admin.register(BloggerModel)
class BloggerAdmin(admin.ModelAdmin):
    fields = ['user', 'name', 'bio_text', 'email', 'birth_date', 'phone_number', 'photo']
    list_filter = ['name', 'register_date',]
    search_fields = ['name', 'user']
    list_display = ['name', 'user', 'register_date']


