# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from devcentryuser.form import DevcentryUserChangeForm, DevcentryUserCreationForm
from devcentryuser.models import DevcentryUser, DevcentryGroupRepos


class DevcentryUserAdmin(UserAdmin):
    form = DevcentryUserChangeForm
    add_form = DevcentryUserCreationForm

    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'second_name', 'last_name', 'user_bio')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser')
        })
    )

    search_fields = ('username', 'email')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')


class DevcentryGroupReposAdmin(admin.ModelAdmin):
    pass


admin.site.register(DevcentryUser, DevcentryUserAdmin)
admin.site.register(DevcentryGroupRepos, DevcentryGroupReposAdmin)
