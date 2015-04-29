# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20150422_1133'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadFile',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profilepic',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
