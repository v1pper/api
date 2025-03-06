from django.urls import path, include
from django.contrib import admin
from api.views import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path('anime/achievements/', anime_achievements),
    path('anime/achievements/completed/', completed_achievements),
    path('anime/<str:tag_name>/<int:anime_id>/achievements/', anime_tag_achievements),
]