from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('music-list/', views.music_list_view, name='music-list'),
    path('music-player/', views.music_player_view, name='music-player'),
    path('images-list/', views.images_list_view, name='images-list'),
    path('images/', views.images_view, name='images'),
]
