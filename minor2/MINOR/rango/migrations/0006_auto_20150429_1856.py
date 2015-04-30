# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_newws'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newws',
            name='news',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
    ]
