# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_ratingposition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'рейтинг', 'verbose_name_plural': 'рейтинги'},
        ),
        migrations.RenameField(
            model_name='ratingposition',
            old_name='rating',
            new_name='rating_o',
        ),
    ]
