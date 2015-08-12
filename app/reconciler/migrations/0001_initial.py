# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term_text', models.CharField(max_length=220)),
                ('add_date', models.DateTimeField(verbose_name=b'date added')),
            ],
        ),
        migrations.CreateModel(
            name='Uri',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri', models.CharField(max_length=500)),
                ('term', models.ForeignKey(to='reconciler.Term')),
            ],
        ),
    ]
