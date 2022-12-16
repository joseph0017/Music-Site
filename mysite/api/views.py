from django.shortcuts import render
from rest_framework import generics, status
from .serializers import MusicSerializer, ImageSerializer
from .models import Music_Player, Images
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination

# Create your views here.


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'music_list_view': '/music-list-view/',
        'music_player_view': '/music-player-view/',
        'images_list_view': '/images-list-view/',
        'images_view': '/images-view/',
    }
    return Response(api_urls)


@api_view(['GET'])
def music_player_view(request, *args, **kwargs):
    qs = Music_Player.objects.all()
    return get_music_paginated_queryset_response(qs, request)


@api_view(['GET'])
def music_list_view(request, *args, **kwargs):
    music_room = Music_Player.objects.all().order_by('-id')
    serializer = MusicSerializer(music_room, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def images_view(request, *args, **kwargs):
    qs = Images.objects.all()
    return get_images_paginated_queryset_response(qs, request)


@api_view(['GET'])
def images_list_view(request, *args, **kwargs):
    pictures = Images.objects.all().order_by('-id')
    serializer = ImageSerializer(pictures, many=True)
    return Response(serializer.data)


def get_music_paginated_queryset_response(qs, request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = MusicSerializer(
        paginated_qs, many=True, context={"request": request})
    # Response( serializer.data, status=200)
    return paginator.get_paginated_response(serializer.data)


def get_images_paginated_queryset_response(qs, request):
    paginator = PageNumberPagination()
    paginator.page_size = 23
    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = ImageSerializer(
        paginated_qs, many=True, context={"request": request})
    # Response( serializer.data, status=200)
    return paginator.get_paginated_response(serializer.data)
