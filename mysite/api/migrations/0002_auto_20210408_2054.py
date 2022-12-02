# Generated by Django 2.2.17 on 2021-04-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='docfile',
            new_name='images',
        ),
        migrations.RemoveField(
            model_name='music_player',
            name='published_date',
        ),
        migrations.AddField(
            model_name='music_player',
            name='album_cover',
            field=models.FileField(default='', upload_to='album_cover/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='music_player',
            name='fast_forward',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='music_player',
            name='rewind',
            field=models.BooleanField(default=False),
        ),
    ]
