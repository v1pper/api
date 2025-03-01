from django.urls import path
from .views import AchievementListView, AchievementDetailView

urlpatterns = [
    path("achievements/", AchievementListView.as_view(), name="achievement_list"),
    path("achievements/<int:pk>/", AchievementDetailView.as_view(), name="achievement_detail"),
]