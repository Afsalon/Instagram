from django.urls import path
from Comment.views import CommentAPI,RemoveCommentAPI

urlpatterns = [
    path('comment/post/', CommentAPI.as_view(), name = "comment_view"),
    path('comment/<int:pk>/', RemoveCommentAPI.as_view(), name="remove_comment")
]
