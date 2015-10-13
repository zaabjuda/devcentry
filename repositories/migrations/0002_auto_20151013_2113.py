# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='g_readers',
            field=models.ManyToManyField(blank=True, to='devcentryuser.DevcentryGroupRepos', related_name='repos_groups_readers'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Repository Name', unique=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='owner',
            field=models.ForeignKey(verbose_name='Repository owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='repository',
            name='r_readers',
            field=models.ManyToManyField(blank=True, to='devcentryuser.DevcentryGroupRepos', related_name='repos_groups_writers'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='readers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, related_name='repos_users_readers'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='repo_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'git'), (2, 'hg')], default=1, verbose_name='VCS Type'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='writers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, related_name='repos_users_writers'),
        ),
    ]
