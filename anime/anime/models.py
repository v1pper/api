from django.db import models

class Achievement(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    completed = models.BooleanField(default=False, verbose_name="Выполнено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.title} - {'Выполнено' if self.completed else 'Не выполнено'}"

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название тега")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class AchievementTag(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, related_name="tags")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.achievement.title} - {self.tag.name}"

    class Meta:
        verbose_name = "Тег достижения"
        verbose_name_plural = "Теги достижений"