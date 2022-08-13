from django.contrib import admin
from .models import User
from .forms import UserEditForm
from django.contrib.auth.admin import UserAdmin


class CustomUser(UserAdmin):
    form = UserEditForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, CustomUser)
