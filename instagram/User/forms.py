from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class UserForm(forms.ModelForm):
    class Meta:
        models = get_user_model()
        fields = "__all__"

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
