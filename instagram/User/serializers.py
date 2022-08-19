from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "password", "profile_picture", "full_name",
                   "email", "website", "bio", "gender", "phone_number"]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["pk","username", "profile_picture", "full_name",
                   "email", "website", "bio", "gender", "phone_number","Following","Followers","Posts","is_public"]

class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "profile_picture", "full_name",
                   "email", "website", "bio", "gender", "phone_number","is_public"]

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    class Meta:
        model = get_user_model()
