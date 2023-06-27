from django.urls import path
from .views import allposts, postdetail

urlpatterns = [
    path('allposts/', allposts),
    path('postdetail/<int:post_id>/', postdetail)
]