from rest_framework import serializers
from Follow.models import Follow

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['pk','user_picture','user_username','user_following','user_following_picture']


class FollowPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['user','following','created_date']
