from django.contrib import admin
from .models import PostModel, CommentModel
from bloggers.models import BloggerModel


class CommentAdmin(admin.StackedInline):
    model = CommentModel
    fields = ['post', 'author', 'text']
    extra = 0


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'blogger', 'likes_count', 'comment_count', 'is_enable']
    list_filter = ['is_enable', 'blogger__name']
    search_fields = ['title']
    list_display_links = ['id', 'title']
    list_editable = ['is_enable']
    readonly_fields = ['likes_count', 'comment_count', 'blogger']

    inlines = [CommentAdmin]

    def save_model(self, request, obj, form, change) -> None:
        obj.blogger = BloggerModel.objects.filter(user=request.user).first()
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(blogger__user=request.user)


@admin.register(BloggerModel)
class BloggerAdmin(admin.ModelAdmin):
    fields = ['user', 'name', 'bio_text', 'email', 'birth_date', 'phone_number', 'photo', 'post_count']
    list_filter = ['name', 'register_date', ]
    search_fields = ['name', 'user']
    readonly_fields = ['post_count']
    list_display = ['name', 'user', 'register_date', 'post_count']

