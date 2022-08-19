from django.urls import path
from Follow.views import FollowAPI,UnFollowAPI,FollowingAPI,FollowedAPI,IsFollowAPI

urlpatterns = [
    path('follow/this/', FollowAPI.as_view(), name = "follow_view"),
    path('follow/<int:pk>/', UnFollowAPI.as_view(), name = "unfollow_view"),
    path('<username>/<int:count>/', FollowingAPI.as_view(), name="following"),
    path('<username>/by/<int:count>/', FollowedAPI.as_view(), name="followed"),
    path('follow/<username>/',IsFollowAPI.as_view(), name="do_i_follow"),
]
