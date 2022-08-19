from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from User.managers import CustomUserManager

GENDER_CHOICES = (
    ('N', "Prefer Not To Say"),
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
)


class User(AbstractUser):
    profile_picture = models.ImageField(
        upload_to="profile_pictures", blank=True, null=True,default="default.png");
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True, null=True)
    bio = models.TextField(max_length=100, blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default="N")
    phone_number = PhoneField(blank=True, null=True)
    first_name = None
    last_name = None
    is_public = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["full_name", "email"]
    USERNAME_FIELD = "username"

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    @property
    def Following(self):
        return self.current_user.all().count()

    @property
    def Followers(self):
        return self.following.all().count()

    @property
    def Posts(self):
        return self.posts_user.all().count()

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "abhishek.genisis@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
