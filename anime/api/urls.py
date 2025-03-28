
from django.urls import path
from .views import (
    anime_achievements,
    completed_achievements,
    anime_tag_achievements,
    create_achievement
)

urlpatterns = [
    path('anime/achievements/', anime_achievements),
    path('anime/achievements/completed/', completed_achievements),
    path('anime/<str:tag_name>/<int:anime_id>/achievements/', anime_tag_achievements),
    path('api/achievements/',create_achievement),
]