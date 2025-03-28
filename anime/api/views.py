from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Anime, Tag, Achievement, AchievementTag

@require_http_methods(["GET"])
def anime_achievements(request):
    achievements = Achievement.objects.all()
    return JsonResponse([a.to_dict() for a in achievements], safe=False)

@require_http_methods(["GET"])
def completed_achievements(request):
    achievements = Achievement.objects.filter(completed=True)
    return JsonResponse([a.to_dict() for a in achievements], safe=False)

@require_http_methods(["GET"])
def anime_tag_achievements(request, tag_name, anime_id):
    try:
        anime = Anime.objects.get(id=anime_id)
        tag = Tag.objects.get(name=tag_name)
        achievements = Achievement.objects.filter(anime=anime, tags=tag)
        return JsonResponse([a.to_dict() for a in achievements], safe=False)
    except (Anime.DoesNotExist, Tag.DoesNotExist):
        return JsonResponse({'error': 'Not found'}, status=404)



@require_http_methods(["POST"])
@csrf_exempt
def create_achievement(request):
    try:
        data = json.loads(request.body)
        anime, _ = Anime.objects.get_or_create(title=data['anime']['title'])
        achievement = Achievement.objects.create(
            anime=anime,
            title=data['title'],
            description=data.get('description', ''),
            completed=data.get('completed', False)
        )
        for tag_name in data.get('tags'):
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            AchievementTag.objects.create(achievement=achievement, tag=tag)
        return JsonResponse(achievement.to_dict(), status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)