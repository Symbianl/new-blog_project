# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_x',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u6ce8\u518c\u7528\u6237',
                'verbose_name_plural': '\u6ce8\u518c\u7528\u6237',
            },
        ),
    ]
