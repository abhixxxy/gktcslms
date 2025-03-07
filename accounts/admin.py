from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    def profile_pic_preview(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="40" height="40" style="border-radius:50%;" />', obj.profile_picture.url)
        return "No Image"

    profile_pic_preview.short_description = "Profile Picture"

    list_display = ("username", "email", "phone", "get_role_display", "profile_pic_preview", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "phone", "role", "profile_picture", "address", "bio")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "first_name", "last_name", "phone", "role", "profile_picture", "address", "bio", "is_staff", "is_active"),
        }),
    )
    search_fields = ("username__icontains", "email__icontains", "phone")
    list_filter = ("role", "is_staff", "is_active")

admin.site.register(CustomUser, CustomUserAdmin)
