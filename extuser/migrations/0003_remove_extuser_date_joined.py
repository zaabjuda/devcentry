# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0002_extgrouprepos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extuser',
            name='date_joined',
        ),
    ]
