# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0003_auto_20150903_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='g_readers',
            field=models.ManyToManyField(to='extuser.ExtGroupRepos', null=True, related_name='repos_groups_readers'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='r_readers',
            field=models.ManyToManyField(to='extuser.ExtGroupRepos', null=True, related_name='repos_groups_writers'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='readers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, related_name='repos_users_readers'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='writers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, related_name='repos_users_writers'),
        ),
    ]
