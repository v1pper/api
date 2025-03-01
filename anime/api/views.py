from django.http import JsonResponse
from django.views import View
from .models import Achievement
import json

class AchievementListView(View):
    def get(self, request, *args, **kwargs):
        achievements = Achievement.objects.all()
        achievements_data = [{"id": a.id, "title": a.title, "description": a.description} for a in achievements]
        return JsonResponse(achievements_data, safe=False)

class AchievementDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            achievement = Achievement.objects.get(id=pk)
            achievement_data = {"id": achievement.id, "title": achievement.title, "description": achievement.description}
            return JsonResponse(achievement_data)
        except Achievement.DoesNotExist:
            return JsonResponse({"error": "Достижение не найдено"}, status=404)