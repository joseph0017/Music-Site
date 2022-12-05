from django.db import models
from django.utils import timezone

# Create your models here.


class Music_Player(models.Model):
    musicSrc = models.FileField(upload_to='music/')
    cover = models.FileField(upload_to='album_cover/')
    pause_song = models.BooleanField(null=False, default=False)
    skip_song = models.BooleanField(null=False, default=False)
    fast_forward = models.BooleanField(null=False, default=False)
    rewind = models.BooleanField(null=False, default=False)
    current_song = models.CharField(max_length=100, null=True)
    duration = models.CharField(max_length=20, default=False)
    name = models.CharField(max_length=100, null=True)
    singer = models.TextField(max_length=1000, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'music'
        verbose_name_plural = 'musics'


class Images(models.Model):
    images = models.FileField(upload_to='images/')
    title = models.CharField(max_length=100, null=True)
    text = models.TextField(max_length=1000, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
