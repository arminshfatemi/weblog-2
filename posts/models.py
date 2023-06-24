from django.db import models
from bloggers.models import BloggerModel
from django.contrib.auth.models import User


class PostModel(models.Model):
    blogger = models.ForeignKey(BloggerModel, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50, )
    text = models.CharField(blank=True, )
    likes_count = models.IntegerField(default=0, )
    comment_count = models.IntegerField(default=0, )
    is_enable = models.BooleanField(default=True, )
    created = models.DateTimeField(auto_now_add=True, )
    photo_main = models.ImageField(upload_to='photos/posts/%Y/%m/%d/', )
    photo_1 = models.ImageField(upload_to='photos/posts/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/posts/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/posts/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/posts/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title
