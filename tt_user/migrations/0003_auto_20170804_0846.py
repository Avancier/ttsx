# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0002_remove_userinfo_uyoubian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uemail',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ushou',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]
