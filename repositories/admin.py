# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib import admin

from repositories.models import Repository


class RepositoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Repository, RepositoryAdmin)
