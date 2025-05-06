# admin.py
from django.contrib import admin
from .models import Anime, Tag, Achievement, AchievementTag

class AchievementTagInline(admin.TabularInline):
    model = Achievement.tags.through 
    extra = 1
    autocomplete_fields = ['tag']

class AchievementInline(admin.StackedInline):
    model = Achievement
    extra = 1
    inlines = [AchievementTagInline]  
    readonly_fields = ('created_at',)

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    inlines = [AchievementInline]  

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [AchievementTagInline]

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'anime', 'completed', 'created_at')
    list_filter = ('completed',)
    search_fields = ('title',)
    inlines = [AchievementTagInline]
    readonly_fields = ('created_at',)  

    fieldsets = (
        (None, {
            'fields': ('anime', 'title', 'description', 'completed', 'created_at')
        }),
    )

@admin.register(AchievementTag)
class AchievementTagAdmin(admin.ModelAdmin):
    list_display = ('achievement', 'tag', 'created_at')
    list_filter = ('tag',)
    search_fields = ('achievement__title', 'tag__name')