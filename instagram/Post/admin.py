from django.contrib import admin
from Post.models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["user", "post_picture", "created_date", "updated_date"]


admin.site.register(Post, PostAdmin)
