from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from userprofile.models import GLMUser


class CustomUserAdmin(UserAdmin):
    # list_display = ("email", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (("User Profile", {"fields": ("balance", "is_premium_user")}),)


admin.site.register(GLMUser, CustomUserAdmin)
