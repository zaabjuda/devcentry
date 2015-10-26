# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internal_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devcentrysshserver',
            name='ip',
            field=models.GenericIPAddressField(unique=True, verbose_name='Server IP'),
        ),
    ]
