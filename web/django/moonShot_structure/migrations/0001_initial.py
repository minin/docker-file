# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Draw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, db_index=True)),
                ('jackpot', models.CharField(max_length=256, null=True, blank=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('date', models.CharField(max_length=256, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lottery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='draw',
            name='lottery',
            field=models.ForeignKey(to='moonShot_structure.Lottery'),
            preserve_default=True,
        ),
    ]
