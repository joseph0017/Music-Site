# Generated by Django 2.2.17 on 2021-04-09 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210408_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='music_player',
            name='duration',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
