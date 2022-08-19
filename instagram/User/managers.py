from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(ugettext_lazy("Email must be provided"))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        if kwargs.get("is_staff") is not True:
            raise ValueError(ugettext_lazy("Not Authorised"))
        if kwargs.get("is_superuser") is not True:
            raise ValueError(ugettext_lazy("Not a superuser"))
        return self.create_user(email, password, **kwargs)
