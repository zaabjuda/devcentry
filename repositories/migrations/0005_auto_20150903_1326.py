# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0004_auto_20150903_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='description',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]
