from django.urls import path
from .views import AchievementAPIView, TagAPIView

urlpatterns = [
    # Для достижений
    path("achievements/", AchievementAPIView.as_view(), name="achievement_api"),
    path("achievements/<int:pk>/", AchievementAPIView.as_view(), name="achievement_detail_api"),
    
    # Для тегов
    path("tags/", TagAPIView.as_view(), name="tag_api"),
    path("tags/<int:pk>/", TagAPIView.as_view(), name="tag_detail_api"),
]