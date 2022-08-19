from django.db import models
from User.models import User
from Post.models import Post
from django.utils import timezone
from crum import get_current_user


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='current_user', editable=False)
    following = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE)
    created_date = models.DateTimeField(editable=False)

    class Meta:
        ordering = ['-created_date']

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_date = timezone.now()
            self.user = user
        return super(Follow, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username + '->' + self.following.username

    @property
    def user_username(self):
        return self.user.username
    @property
    def user_following(self):
        return self.following.username
    @property
    def user_picture(self):
        return self.user.profile_picture.url
    @property
    def user_following_picture(self):
        return self.following.profile_picture.url
