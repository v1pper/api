from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Achievement, Tag, AchievementTag
import json
from django.db import transaction

@method_decorator(csrf_exempt, name='dispatch')
class AchievementAPIView(View):
    
    
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            # Детали одного достижения
            try:
                achievement = Achievement.objects.get(id=pk)
                tags = self._get_achievement_tags(achievement)
                
                return JsonResponse({
                    "id": achievement.id,
                    "title": achievement.title,
                    "description": achievement.description,
                    "completed": achievement.completed,
                    "tags": tags,
                    "created_at": achievement.created_at,
                    "updated_at": achievement.updated_at
                })
            except Achievement.DoesNotExist:
                return JsonResponse({"error": "Достижение не найдено"}, status=404)
        else:
            # Список всех достижений с фильтрацией
            achievements = Achievement.objects.all()
            
            # Фильтр по статусу completed
            if 'completed' in request.GET:
                achievements = achievements.filter(
                    completed=request.GET['completed'].lower() == 'true'
                )
            
            # Фильтр по тегу
            if 'tag' in request.GET:
                achievements = achievements.filter(
                    tags__tag__id=request.GET['tag']
                ).distinct()
            
            achievements_data = []
            for achievement in achievements:
                tags = self._get_achievement_tags(achievement)
                achievements_data.append({
                    "id": achievement.id,
                    "title": achievement.title,
                    "completed": achievement.completed,
                    "tags": tags
                })
            
            return JsonResponse(achievements_data, safe=False)

    def post(self, request, *args, **kwargs):
        # Создание достижения
        try:
            data = json.loads(request.body)
            
            with transaction.atomic():
                achievement = Achievement.objects.create(
                    title=data['title'],
                    description=data.get('description', ''),
                    completed=data.get('completed', False)
                )
                
                if 'tags' in data:
                    self._process_tags(achievement, data['tags'])
                
                return JsonResponse({
                    "id": achievement.id,
                    "message": "Достижение создано",
                    "tags": self._get_achievement_tags(achievement)
                }, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def put(self, request, pk=None, *args, **kwargs):
        # Обновление достижения
        if not pk:
            return JsonResponse({"error": "Требуется ID достижения"}, status=400)
        
        try:
            data = json.loads(request.body)
            achievement = Achievement.objects.get(id=pk)
            
            with transaction.atomic():
                achievement.title = data.get('title', achievement.title)
                achievement.description = data.get('description', achievement.description)
                achievement.completed = data.get('completed', achievement.completed)
                achievement.save()
                
                if 'tags' in data:
                    AchievementTag.objects.filter(achievement=achievement).delete()
                    self._process_tags(achievement, data['tags'])
                
                return JsonResponse({
                    "id": achievement.id,
                    "message": "Достижение обновлено",
                    "tags": self._get_achievement_tags(achievement)
                })
        except Achievement.DoesNotExist:
            return JsonResponse({"error": "Достижение не найдено"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def delete(self, request, pk=None, *args, **kwargs):
        # Удаление достижения
        if not pk:
            return JsonResponse({"error": "Требуется ID достижения"}, status=400)
        
        try:
            achievement = Achievement.objects.get(id=pk)
            achievement.delete()
            return JsonResponse({"message": "Достижение удалено"})
        except Achievement.DoesNotExist:
            return JsonResponse({"error": "Достижение не найдено"}, status=404)

    def _get_achievement_tags(self, achievement):
        """Получает теги для достижения"""
        return [{
            "id": at.tag.id,
            "name": at.tag.name
        } for at in AchievementTag.objects.filter(achievement=achievement).select_related('tag')]

    def _process_tags(self, achievement, tag_ids):
        """Обрабатывает привязку тегов к достижению"""
        for tag_id in tag_ids:
            tag = Tag.objects.get(id=tag_id)
            AchievementTag.objects.create(achievement=achievement, tag=tag)

@method_decorator(csrf_exempt, name='dispatch')
class TagAPIView(View):
    
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            # Детали одного тега
            try:
                tag = Tag.objects.get(id=pk)
                return JsonResponse({
                    "id": tag.id,
                    "name": tag.name,
                    "achievements": [{
                        "id": at.achievement.id,
                        "title": at.achievement.title
                    } for at in AchievementTag.objects.filter(tag=tag).select_related('achievement')]
                })
            except Tag.DoesNotExist:
                return JsonResponse({"error": "Тег не найден"}, status=404)
        else:
            # Список всех тегов
            tags = Tag.objects.all()
            tags_data = [{
                "id": tag.id,
                "name": tag.name,
                "achievement_count": AchievementTag.objects.filter(tag=tag).count()
            } for tag in tags]
            return JsonResponse(tags_data, safe=False)

    def post(self, request, *args, **kwargs):
        # Создание тега
        try:
            data = json.loads(request.body)
            tag = Tag.objects.create(name=data['name'])
            return JsonResponse({
                "id": tag.id,
                "name": tag.name
            }, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def put(self, request, pk=None, *args, **kwargs):
        # Обновление тега
        if not pk:
            return JsonResponse({"error": "Требуется ID тега"}, status=400)
        
        try:
            tag = Tag.objects.get(id=pk)
            data = json.loads(request.body)
            tag.name = data.get('name', tag.name)
            tag.save()
            return JsonResponse({
                "id": tag.id,
                "name": tag.name
            })
        except Tag.DoesNotExist:
            return JsonResponse({"error": "Тег не найден"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def delete(self, request, pk=None, *args, **kwargs):
        # Удаление тега
        if not pk:
            return JsonResponse({"error": "Требуется ID тега"}, status=400)
        
        try:
            tag = Tag.objects.get(id=pk)
            tag.delete()
            return JsonResponse({"message": "Тег удален"})
        except Tag.DoesNotExist:
            return JsonResponse({"error": "Тег не найден"}, status=404)