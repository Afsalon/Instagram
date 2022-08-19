from django.contrib import admin
from User.models import User
from django.contrib.auth.admin import UserAdmin
from User.forms import UserForm
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    model = get_user_model()
    list_display = ["username", "email", "full_name", "is_staff","Following","Followers"]
    add_fieldsets = (
        ('Personal Details', {
         'fields': ("username", "password", "profile_picture", "full_name",
                    "email", "website", "bio", "gender", "phone_number","is_public")}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    fieldsets = (
        (
            ('Personal Details', {
             'fields': ("username", "password", "profile_picture", "full_name",
                        "email", "website", "bio", "gender", "phone_number","is_public")}),
            ('Permissions', {'fields': ('is_staff', 'is_active')})
        )
    )


admin.site.register(User, CustomUserAdmin)
