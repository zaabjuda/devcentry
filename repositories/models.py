# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from enum import Enum, unique

from django.db import models
from django.utils.translation import ugettext_lazy as _

from devcentryuser.models import DevcentryUser, DevcentryGroupRepos


@unique
class VcsTypes(Enum):
    git = 1
    hg = 2


class Repository(models.Model):
    VCS_TYPES = (tuple((member.value, name)) for name, member in VcsTypes.__members__.items())

    name = models.CharField(verbose_name=_("Repository Name"), max_length=250, unique=True, null=False)
    repo_type = models.PositiveSmallIntegerField(verbose_name=_("VCS Type"), null=False, choices=VCS_TYPES,
                                                 default=VcsTypes.git.value)
    owner = models.ForeignKey(DevcentryUser, null=False, verbose_name=_("Repository owner"))
    readers = models.ManyToManyField(DevcentryUser, related_name='repos_users_readers', blank=True)
    writers = models.ManyToManyField(DevcentryUser, related_name='repos_users_writers', blank=True)
    read_only = models.BooleanField(default=False)
    description = models.CharField(max_length=2048, null=True)
    g_readers = models.ManyToManyField(DevcentryGroupRepos, related_name='repos_groups_readers', blank=True)
    r_readers = models.ManyToManyField(DevcentryGroupRepos, related_name='repos_groups_writers', blank=True)
