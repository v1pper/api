from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import Achievement  # Используем относительный импорт

class AchievementListView(View):
    def get(self, request: HttpRequest):
        achievements = Achievement.objects.all()
        data = [{"title": ach.title, "completed": ach.completed} for ach in achievements]
        return JsonResponse(data, safe=False)

class AchievementDetailView(View):
    def get(self, request: HttpRequest, pk: int):
        achievement = Achievement.objects.get(pk=pk)
        data = {
            "title": achievement.title,
            "description": achievement.description,
            "completed": achievement.completed,
        }
        return JsonResponse(data)