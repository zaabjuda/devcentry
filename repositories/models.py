# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from enum import Enum, unique

from django.db import models

from devcentryuser.models import DevcentryUser, DevcentryGroupRepos


@unique
class VcsTypes(Enum):
    git = 1
    hg = 2


class Repository(models.Model):
    VCS_TYPES = (tuple((member.value, name)) for name, member in VcsTypes.__members__.items())

    name = models.CharField(max_length=250, unique=True, null=False)
    repo_type = models.PositiveSmallIntegerField(null=False, choices=VCS_TYPES, default=VcsTypes.git.value)
    owner = models.ForeignKey(DevcentryUser, null=False)
    readers = models.ManyToManyField(DevcentryUser, related_name='repos_users_readers')
    writers = models.ManyToManyField(DevcentryUser, related_name='repos_users_writers')
    read_only = models.BooleanField(default=False)
    description = models.CharField(max_length=2048, null=True)
    g_readers = models.ManyToManyField(DevcentryGroupRepos, related_name='repos_groups_readers')
    r_readers = models.ManyToManyField(DevcentryGroupRepos, related_name='repos_groups_writers')
