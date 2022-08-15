from django.contrib import admin
from .models import User
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin


class CustomUser(UserAdmin):
    add_form = UserChangeForm
    form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email", "image", 'phone')}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {'fields': (
            'phone', 'email', 'first_name', 'last_name', 'password', 'image')}
         ),
    )

    list_display = ('first_name', 'is_superuser', 'email')
    list_filter = ('is_superuser', "is_staff")
    list_editable = ()


admin.site.register(User, CustomUser)
