
from django.urls import path
<<<<<<< HEAD
from .views import AchievementAPIView, TagAPIView

urlpatterns = [
    # Для достижений
    path("achievements/", AchievementAPIView.as_view(), name="achievement_api"),
    path("achievements/<int:pk>/", AchievementAPIView.as_view(), name="achievement_detail_api"),
    
    # Для тегов
    path("tags/", TagAPIView.as_view(), name="tag_api"),
    path("tags/<int:pk>/", TagAPIView.as_view(), name="tag_detail_api"),
=======
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
>>>>>>> ca88e7910aa161598d49bac1b65aacb816dc4efd
]