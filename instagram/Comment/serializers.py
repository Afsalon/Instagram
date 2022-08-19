from rest_framework import serializers
from Comment.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["pk","text","post","user_comment","user_picture","created_date","is_deletable"]

class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["pk","text","post","user_comment","user_picture","created_date"]
        # fields = '__all__'
