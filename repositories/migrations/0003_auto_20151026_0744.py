# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repositories', '0002_auto_20151013_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepositoryNameSpace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, verbose_name='Name', max_length=250)),
                ('is_project', models.BooleanField(verbose_name='Is projects')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Namespace owner')),
            ],
            options={
                'verbose_name_plural': 'Repositories Namespaces',
                'verbose_name': 'Repository Namespace',
            },
        ),
        migrations.AlterModelOptions(
            name='repository',
            options={'verbose_name_plural': 'Repositories', 'verbose_name': 'Repository'},
        ),
        migrations.AlterField(
            model_name='repository',
            name='repo_type',
            field=models.CharField(default='git', choices=[('git', 'git')], verbose_name='VCS Type', max_length=5),
        ),
        migrations.AddField(
            model_name='repository',
            name='name_space',
            field=models.ForeignKey(to='repositories.RepositoryNameSpace', default=1, verbose_name='Repository Namespace'),
            preserve_default=False,
        ),
    ]
