# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20150503_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newws',
            name='latitude',
            field=models.DecimalField(max_digits=31, decimal_places=10),
        ),
        migrations.AlterField(
            model_name='newws',
            name='longitude',
            field=models.DecimalField(max_digits=31, decimal_places=10),
        ),
    ]
