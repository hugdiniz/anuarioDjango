# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0006_auto_20141211_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='oucupante',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cargo',
            field=models.ForeignKey(default=1, to='yearbook.Cargo'),
            preserve_default=False,
        ),
    ]
