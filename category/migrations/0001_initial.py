# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('create_time', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]
