# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-22 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0011_remove_anxietyscore_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anxietyscorecard',
            name='score_after_20_min',
        ),
        migrations.AddField(
            model_name='anxietyscorecard',
            name='anxiety_at_0_min',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_0', to='challenges.AnxietyScore'),
        ),
        migrations.AddField(
            model_name='anxietyscorecard',
            name='anxiety_at_30_min',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_30', to='challenges.AnxietyScore'),
        ),
        migrations.AddField(
            model_name='anxietyscorecard',
            name='anxiety_at_60_min',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_60', to='challenges.AnxietyScore'),
        ),
    ]
