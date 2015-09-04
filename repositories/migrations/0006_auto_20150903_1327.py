# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0005_auto_20150903_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='g_readers',
            field=models.ManyToManyField(related_name='repos_groups_readers', to='extuser.ExtGroupRepos'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='r_readers',
            field=models.ManyToManyField(related_name='repos_groups_writers', to='extuser.ExtGroupRepos'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='readers',
            field=models.ManyToManyField(related_name='repos_users_readers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='repository',
            name='writers',
            field=models.ManyToManyField(related_name='repos_users_writers', to=settings.AUTH_USER_MODEL),
        ),
    ]
