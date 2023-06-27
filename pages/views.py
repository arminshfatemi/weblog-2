# from django.http.response import HttpResponse

from django.shortcuts import render, get_object_or_404
from posts.models import PostModel, CommentModel
from django.db.models import Q


def allposts(request):
    post = PostModel.objects.order_by('-created_time').filter(is_enable=True)
    return render(request, 'posts/posts.html', context={'post': post})


def postdetail(request, post_id):
    post = get_object_or_404(PostModel, pk=post_id)
    comment = CommentModel.objects.filter(post=post).all()
    context = {
        'post': post,
        'comment': comment,
    }
    return render(request, 'posts/postdetail.html', context=context)


def search(request):
    posts = PostModel.objects.order_by('-created_time').filter(is_enable=True)
    if 'search_text' in request.GET:
        search_text = request.GET['search_text']
        print(search_text)

        if search_text:
            posts = posts.filter(Q(title__icontains=search_text)
                                 | Q(blogger__name__icontains=search_text)
                                 | Q(text__icontains=search_text))
            print(posts)

    context = {
        'posts': posts
    }
    return render(request, 'posts/search.html', context=context)
