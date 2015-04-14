# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('newstreet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='change_password',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favourite_hamster_name',
            field=models.CharField(default=b'none!', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='likes_cheese',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
