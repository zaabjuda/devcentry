# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0006_auto_20150903_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='repo_type',
            field=models.PositiveSmallIntegerField(default=1, choices=[(1, 'git'), (2, 'hg')]),
        ),
    ]
