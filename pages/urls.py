from django.urls import path
from .views import allposts, postdetail, search

urlpatterns = [
    path('allposts/', allposts),
    path('postdetail/<int:post_id>/', postdetail),
    path('search/', search, name='search'),
]
