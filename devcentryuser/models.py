# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

import os

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class DevcentryUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('User must have email')
        if not username:
            raise ValueError('User must have username')
        user = self.model(username=username, email=self.normalize_email(email))
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class DevcentryUser(AbstractBaseUser, PermissionsMixin):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')

    username = models.CharField(unique=True, max_length=30, validators=[alphanumeric])
    email = models.EmailField(verbose_name='email field', unique=True, max_length=255)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    second_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, null=False)
    is_staff = models.BooleanField(default=False, null=False)

    user_bio = models.TextField()

    objects = DevcentryUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return '%s %s %s'.format(self.last_name, self.first_name, self.second_name)

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email


class DevcentryGroupRepos(models.Model):
    name = models.CharField(max_length=250, unique=True)
    users = models.ManyToManyField(DevcentryUser)


@receiver(post_save, sender=DevcentryUser)
def create_repo(sender, instance, created, **kwargs):
    if created:
        from repositories.models import RepositoryNameSpace
        ns = RepositoryNameSpace(name=instance.username, is_project=False, owner=instance)
        if not os.path.exists(ns.abs_path):
                os.mkdir(ns.abs_path)
        else:
            raise Exception
        ns.save()
