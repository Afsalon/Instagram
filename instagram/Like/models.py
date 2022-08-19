from django.db import models
from User.models import User
from Post.models import Post
from django.utils import timezone
from crum import get_current_user


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, editable=False)
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
        return super(Like, self).save(*args, **kwargs)

    def __str__(self):
        return (str(self.pk))
