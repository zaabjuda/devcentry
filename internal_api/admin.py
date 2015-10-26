# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"


from django.contrib import admin

from internal_api.models import DevCentrySSHServer


class DevCentrySSHServerAdmin(admin.ModelAdmin):
    pass


admin.site.register(DevCentrySSHServer, DevCentrySSHServerAdmin)
