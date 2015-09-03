# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0002_extgrouprepos'),
        ('repositories', '0002_auto_20150903_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='g_readers',
            field=models.ManyToManyField(related_name='repos_groups_readers', to='extuser.ExtGroupRepos'),
        ),
        migrations.AddField(
            model_name='repository',
            name='r_readers',
            field=models.ManyToManyField(related_name='repos_groups_writers', to='extuser.ExtGroupRepos'),
        ),
    ]
