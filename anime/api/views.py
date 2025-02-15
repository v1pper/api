from django.shortcuts import render
from .models import Achievement
from django.hhtp import HttpRequest, JsonResponse



class AchievementListView(ListView):
    model = Achievement
    template_name = "achievements/achievement_list.html"
    context_object_name = "achievements"


class AchievementDetailView(DetailView):
    model = Achievement
    template_name = "achievements/achievement_detail.html"
    context_object_name = "achievement"

def achievement(request: HttpRequest):
    if request.method == "GET":

        achievement = City.objects().take(1)
        return JsonResponse(city,safe = False, encoder = JSONEncoder)

