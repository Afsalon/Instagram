from rest_framework import serializers
from Post.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["pk","user","post_picture", "caption", "Likes","Comments","updated_date","user_username","user_profile_picture"]
