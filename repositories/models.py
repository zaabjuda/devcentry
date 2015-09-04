# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from enum import Enum, unique

from django.db import models

from extuser.models import ExtUser, ExtGroupRepos


@unique
class VcsTypes(Enum):
    git = 1
    hg = 2


class Repository(models.Model):
    VCS_TYPES = (tuple((member.value, name)) for name, member in VcsTypes.__members__.items())

    name = models.CharField(max_length=250, unique=True, null=False)
    repo_type = models.PositiveSmallIntegerField(null=False, choices=VCS_TYPES, default=VcsTypes.git.value)
    owner = models.ForeignKey(ExtUser, null=False)
    readers = models.ManyToManyField(ExtUser, related_name='repos_users_readers')
    writers = models.ManyToManyField(ExtUser, related_name='repos_users_writers')
    read_only = models.BooleanField(default=False)
    description = models.CharField(max_length=2048, null=True)
    g_readers = models.ManyToManyField(ExtGroupRepos, related_name='repos_groups_readers')
    r_readers = models.ManyToManyField(ExtGroupRepos, related_name='repos_groups_writers')
