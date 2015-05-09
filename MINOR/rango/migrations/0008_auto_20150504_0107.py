# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20150504_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newws',
            name='latitude',
            field=models.DecimalField(max_digits=41, decimal_places=20),
        ),
        migrations.AlterField(
            model_name='newws',
            name='longitude',
            field=models.DecimalField(max_digits=41, decimal_places=20),
        ),
    ]
