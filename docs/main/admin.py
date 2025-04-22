from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', '封禁状态')
 
    def 封禁状态(self, obj):
        return not obj.is_active
 
    封禁状态.boolean = True
 
    def ban_users(modeladmin, request, queryset):
        if not request.user.is_superuser:
            raise PermissionDenied("Only superusers can ban users.")
        queryset.update(is_active=False)
    def unban_users(modeladmin, request, queryset):
        if not request.user.is_superuser:
            raise PermissionDenied("Only superusers can ban users.")
        queryset.update(is_active=True)
    ban_users.short_description = "封禁所选的 用户"
    unban_users.short_description = "解封所选的 用户"
    actions = [ban_users,unban_users]
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(School)
admin.site.register(Class)
admin.site.register(Activity)