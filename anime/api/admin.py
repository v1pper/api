from django.contrib import admin
from .models import Achievement, Tag, AchievementTag

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "created_at")
    list_filter = ("completed",)
    search_fields = ("title", "description")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(AchievementTag)
class AchievementTagAdmin(admin.ModelAdmin):
    list_display = ("achievement", "tag")
    list_filter = ("tag",)