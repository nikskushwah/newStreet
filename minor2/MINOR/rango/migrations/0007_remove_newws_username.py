# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20150429_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newws',
            name='username',
        ),
    ]
