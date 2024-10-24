# Generated by Django 5.1.2 on 2024-10-23 16:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questions',
            name='createdAt',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
