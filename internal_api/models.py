# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

import random
import string

from django.core import signing
from django.db.models.signals import pre_save
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class DevCentrySSHServer(models.Model):
    name = models.CharField(verbose_name=_('Server name'), max_length=40, null=False, blank=False, unique=True)
    ip = models.GenericIPAddressField(verbose_name=_('Server IP'), null=False, blank=False, unique=True)
    uniq_key = models.CharField(verbose_name=_('Unique key'), max_length=11)
    access_token = models.CharField(verbose_name=_('Access token'), max_length=128)

    def __str__(self):
        return "{} IP: {}".format(self.name, self.ip)

    def to_sign(self):
        return dict(ip=self.ip)

    class Meta:
        verbose_name = _('DevCentry SSH Server')
        verbose_name_plural = _('DevCentry SSH Servers')


@receiver(pre_save, sender=DevCentrySSHServer)
def create_access_token(sender, instance, **kwargs):
    if not instance.pk:
        u_k = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(11))
        instance.uniq_key = u_k
        instance.access_token = signing.dumps(instance.to_sign(), key=instance.uniq_key)[:128]
