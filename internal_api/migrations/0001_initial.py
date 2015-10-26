# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevCentrySSHServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Server name', max_length=40, unique=True)),
                ('ip', models.IPAddressField(verbose_name='Server IP', unique=True)),
                ('uniq_key', models.UUIDField(verbose_name='Unique key')),
                ('access_token', models.CharField(verbose_name='Access token', max_length=128)),
            ],
            options={
                'verbose_name': 'DevCentry SSH Server',
                'verbose_name_plural': 'DevCentry SSH Servers',
            },
        ),
    ]
