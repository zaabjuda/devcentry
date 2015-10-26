# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

import os

from dulwich.repo import Repo
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from devcentryuser.models import DevcentryUser, DevcentryGroupRepos

VCS_TYPES = (('git', 'git'),)


class RepositoryNameSpace(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=250, unique=True, null=False)
    is_project = models.BooleanField(verbose_name=_('Is projects'))
    owner = models.ForeignKey(DevcentryUser, null=False, verbose_name=_("Namespace owner"))

    @property
    def abs_path(self):
        return os.path.abspath(os.path.join(settings.VCS_REPO_DIR, self.name))

    def __str__(self):
        return "{} Owner: {}".format(self.name, self.owner)

    class Meta:
        verbose_name = _("Repository Namespace")
        verbose_name_plural = _("Repositories Namespaces")


class Repository(models.Model):
    name = models.CharField(verbose_name=_("Repository Name"), max_length=250, unique=True, null=False)
    repo_type = models.CharField(verbose_name=_("VCS Type"), null=False, choices=VCS_TYPES, max_length=5,
                                 default='git')
    owner = models.ForeignKey(DevcentryUser, null=False, verbose_name=_("Repository owner"))
    readers = models.ManyToManyField(DevcentryUser, related_name='repos_users_readers', blank=True)
    writers = models.ManyToManyField(DevcentryUser, related_name='repos_users_writers', blank=True)
    read_only = models.BooleanField(default=False)
    description = models.CharField(max_length=2048, null=True)
    g_readers = models.ManyToManyField(DevcentryGroupRepos, related_name='repos_groups_readers', blank=True)
    r_readers = models.ManyToManyField(DevcentryGroupRepos, related_name='repos_groups_writers', blank=True)
    name_space = models.ForeignKey(RepositoryNameSpace, null=False, verbose_name=_("Repository Namespace"))

    @property
    def repo_path(self):
        return "{}/{}.{}".format(self.name_space.name, self.name, self.repo_type)

    @property
    def abs_path(self):
        return os.path.abspath(os.path.join(settings.VCS_REPO_DIR, self.repo_path))

    def __str__(self):
        return "{} ({})".format(self.name, self.repo_type)

    class Meta:
        verbose_name = _("Repository")
        verbose_name_plural = _("Repositories")


@receiver(pre_save, sender=Repository)
def create_repo(sender, instance, **kwargs):
    if not instance.pk:
        if not os.path.exists(instance.abs_path):
            os.mkdir(instance.abs_path)
            Repo.init_bare(instance.abs_path)
