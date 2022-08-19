from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Post.urls')),
    path('', include('User.urls')),
    path('', include('Like.urls')),
    path('', include('Comment.urls')),
    path('', include('Follow.urls')),

]
