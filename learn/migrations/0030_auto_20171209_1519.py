# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-09 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0029_resource_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.IntegerField(choices=[(1, 'Upvote'), (-1, 'DownVote')], default=1),
        ),
    ]
