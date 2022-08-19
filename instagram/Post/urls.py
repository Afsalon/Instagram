from os import stat
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Post.views import PostAPI,PostDetailAPI,ProfilePostAPI,PostPostAPI
urlpatterns = [
    path('posts/<int:count>/', PostAPI.as_view(), name = "all_post_page"),
    path('posts/', PostPostAPI.as_view(), name = "post_post_page"),
    path('post/<int:pk>/',PostDetailAPI.as_view(), name="post_detail_page"),
    path('post/<username>/',ProfilePostAPI.as_view(), name="profile_post_page"),
]


urlpatterns.extend(
    static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
)
