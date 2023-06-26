from django.urls import path
from .views import allposts

urlpatterns = [
    path('allposts/', allposts)
]