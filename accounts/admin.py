from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustumUserCreationForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustumUserCreationForm
    model = CustomUser
    list_display = ["username", "email", "age", "is_staff", "password"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("age",)}),

    )


admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
