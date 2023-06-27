# from django.http.response import HttpResponse

from django.shortcuts import render, get_object_or_404
from posts.models import PostModel, CommentModel


def allposts(request):
    post = PostModel.objects.order_by('-created_time').filter(is_enable=True)
    return render(request, 'posts.html', context={'post': post})


def postdetail(request, post_id):
    post = get_object_or_404(PostModel, pk=post_id)
    comment = CommentModel.objects.filter(post=post).all()
    context = {
        'post': post,
        'comment': comment,
    }
    return render(request, 'postdetail.html', context=context)


