# Generated by Django 4.1.3 on 2022-12-05 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_music_player_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music_player',
            name='duration',
            field=models.DurationField(default=True),
        ),
    ]