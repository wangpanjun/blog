# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('create_time', models.DateField(auto_created=True)),
                ('art_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, db_index=True, null=True)),
                ('content', models.TextField()),
                ('update_time', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
