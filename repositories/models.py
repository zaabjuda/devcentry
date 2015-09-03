# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.db import models

from extuser.models import ExtUser, ExtGroupRepos


class Repository(models.Model):
    name = models.CharField(max_length=250, unique=True)
    repo_type = models.PositiveSmallIntegerField()
    owner = models.ForeignKey(ExtUser)
    readers = models.ManyToManyField(ExtUser, related_name='repos_users_readers')
    writers = models.ManyToManyField(ExtUser, related_name='repos_users_writers')
    read_only = models.BooleanField(default=False)
    description = models.CharField(max_length=2048)
    g_readers = models.ManyToManyField(ExtGroupRepos, related_name='repos_groups_readers')
    r_readers = models.ManyToManyField(ExtGroupRepos, related_name='repos_groups_writers')
