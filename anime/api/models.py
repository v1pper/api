
from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Achievement(models.Model):
    anime = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE,
        related_name='achievements'
    )
    tags = models.ManyToManyField(
        Tag,
        through='AchievementTag',  
        related_name='achievements'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.anime.title})"

class AchievementTag(models.Model):
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        related_name='tag_links'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='achievement_links'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('achievement', 'tag')
    
    def __str__(self):
        return f"{self.achievement} - {self.tag}"