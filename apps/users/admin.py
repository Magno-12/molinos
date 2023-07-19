from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.users.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'full_name', 'is_active', 'is_staff', 'is_admin', 'is_superuser', 'role')
    list_filter = ('is_active', 'is_staff', 'is_admin', 'is_superuser', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'full_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'full_name', 'role', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'username', 'full_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
