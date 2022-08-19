from django.contrib import admin
from Follow.models import Follow


class FollowAdmin(admin.ModelAdmin):
    model = Follow
    list_display = ['user','following','created_date']


admin.site.register(Follow, FollowAdmin)
