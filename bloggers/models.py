from django.db import models
from django.contrib.auth.models import User


class BloggerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    bio_text = models.TextField(blank=True,)
    name = models.CharField(blank=False, max_length=100)
    birth_date = models.DateField(blank=True)
    register_date = models.DateTimeField(auto_now_add=True,)
    post_count = models.IntegerField(default=0)
    email = models.CharField(blank=False, max_length=100)
    phone_number = models.CharField(blank=True, max_length=50)
    photo = models.ImageField(upload_to='photos/bloggers/%Y/%m/%d/')

    def __str__(self):
        return self.name