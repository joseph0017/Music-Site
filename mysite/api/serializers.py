from .models import Music_Player, Images
from rest_framework import serializers


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music_Player
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
