# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='repo_type',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
