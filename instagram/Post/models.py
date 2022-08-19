from django.db import models
from User.models import User
from django.utils import timezone
from crum import get_current_user

class Post(models.Model):
    post_picture = models.ImageField(upload_to="posts")
    user = models.ForeignKey(
        User, related_name='posts_user',on_delete=models.CASCADE, editable=False)
    caption = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)

    class Meta:
        ordering = ['-created_date']

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_date = timezone.now()
            self.user = user
        self.updated_date = timezone.now()
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return (str(self.pk))

    @property
    def Likes(self):
        return self.likes.all().count()

    @property
    def Comments(self):
        return self.comments.all().count()
    @property
    def user_username(self):
         return User.objects.get(pk = self.user.pk).username

    @property
    def user_profile_picture(self):
         return str(User.objects.get(pk = self.user.pk).profile_picture)
