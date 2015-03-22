# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20150321_1457'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
