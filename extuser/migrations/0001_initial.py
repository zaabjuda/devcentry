# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')], max_length=30, unique=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email field', unique=True)),
                ('first_name', models.CharField(max_length=50, null=True, blank=True)),
                ('second_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('user_bio', models.TextField()),
                ('groups', models.ManyToManyField(related_name='user_set', verbose_name='groups', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', verbose_name='user permissions', related_query_name='user', help_text='Specific permissions for this user.', blank=True, to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
