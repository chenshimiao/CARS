# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('title', models.TextField()),
                ('distance', models.IntegerField()),
                ('price', models.IntegerField()),
                ('time', models.TextField()),
                ('city', models.TextField()),
                ('gearbox', models.TextField()),
            ],
        ),
    ]
