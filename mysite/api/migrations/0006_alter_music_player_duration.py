# Generated by Django 4.1.3 on 2022-12-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_music_player_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music_player',
            name='duration',
            field=models.CharField(max_length=100, null=True),
        ),
    ]