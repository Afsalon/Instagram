from django.db import models
from User.models import User
from Post.models import Post
from django.utils import timezone
from crum import get_current_user


class Comment(models.Model):
    text = models.TextField(max_length=300)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, editable=False)
    created_date = models.DateTimeField(editable=False)

    class Meta:
        ordering = ['created_date']

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_date = timezone.now()
            self.user = user
        return super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return (str(self.pk))

    @property
    def user_comment(self):
        return self.user.username

    @property
    def user_picture(self):
        return self.user.profile_picture.url

    @property
    def is_deletable(self):
        user = get_current_user()
        post_obj = Post.objects.get(pk = self.post.pk)
        if user.pk == post_obj.user.pk:
            return True
        elif user.pk == self.user.pk:
            return True
        else:
            return False
