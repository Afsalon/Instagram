from django.contrib import admin
from Like.models import Like


class LikeAdmin(admin.ModelAdmin):
    model = Like
    list_display = ["user", "post", "created_date"]


admin.site.register(Like, LikeAdmin)
