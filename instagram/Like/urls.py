from django.urls import path
from Like.views import LikeAPI,RemoveLikeAPI
urlpatterns = [
    path('like/this/post/', LikeAPI.as_view(), name = "like_view"),
    path('like/<int:pk>/', RemoveLikeAPI.as_view(), name="dislike")
]
