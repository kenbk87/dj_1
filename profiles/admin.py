from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

User = get_user_model()


@admin.register(User)
class ProfilesUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'year_birth', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_( 'Personal info' ), {'fields': (
            'full_name',
            'email',
            'year_birth',
            'address',
            'about')}),
        (_( 'Permissions' ), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_( 'Important dates' ), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email'),
        }),
    )
    search_fields = ('username', 'full_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
