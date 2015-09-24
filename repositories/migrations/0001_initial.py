# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devcentryuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('repo_type', models.PositiveSmallIntegerField(choices=[(1, 'git'), (2, 'hg')], default=1)),
                ('read_only', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=2048, null=True)),
                ('g_readers', models.ManyToManyField(to='devcentryuser.DevcentryGroupRepos', related_name='repos_groups_readers')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('r_readers', models.ManyToManyField(to='devcentryuser.DevcentryGroupRepos', related_name='repos_groups_writers')),
                ('readers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='repos_users_readers')),
                ('writers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='repos_users_writers')),
            ],
        ),
    ]
