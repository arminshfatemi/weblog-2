from django.shortcuts import render
from posts.models import PostModel, CommentModel


def allposts(request):
    post = PostModel.objects.all()
    return render(request, 'posts.html', context={'post': post})
