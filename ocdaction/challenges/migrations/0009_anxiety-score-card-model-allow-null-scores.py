# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-17 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0008_anxiety-score-card-model-delete-user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anxietyscorecard',
            name='anxiety_at_10_min',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_10', to='challenges.AnxietyScore'),
        ),
        migrations.AlterField(
            model_name='anxietyscorecard',
            name='anxiety_at_15_min',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_15', to='challenges.AnxietyScore'),
        ),
        migrations.AlterField(
            model_name='anxietyscorecard',
            name='score_after_20_min',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_20', to='challenges.AnxietyScore'),
        ),
        migrations.AlterField(
            model_name='anxietyscorecard',
            name='anxiety_at_5_min',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='score_5', to='challenges.AnxietyScore'),
        ),
    ]
