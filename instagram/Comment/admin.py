from django.contrib import admin
from Comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ["user", "post", "created_date","user_comment"];


admin.site.register(Comment, CommentAdmin)
