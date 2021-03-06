# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateField(default='2017-09-29'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='_user_friends_+', to='logreg.User'),
        ),
    ]
