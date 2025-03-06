
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from .models import Achievement,Anime,Tag
import json


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
        achievements = Achievement.objects.filter(
            anime=anime,
            tags=tag
        )
        return JsonResponse([a.to_dict() for a in achievements], safe=False)
    except (Anime.DoesNotExist, Tag.DoesNotExist):
        return JsonResponse({'error': 'Not found'}, status=404)


