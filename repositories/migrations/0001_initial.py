# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=250)),
                ('repo_type', models.IntegerField(max_length=1)),
                ('read_only', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=2048)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('readers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='repos_users_readers')),
                ('writers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='repos_users_writers')),
            ],
        ),
    ]
