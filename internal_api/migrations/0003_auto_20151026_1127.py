# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internal_api', '0002_auto_20151026_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devcentrysshserver',
            name='uniq_key',
            field=models.CharField(verbose_name='Unique key', max_length=11),
        ),
    ]
