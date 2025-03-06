# Generated by Django 5.1.6 on 2025-03-06 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='api.anime')),
            ],
        ),
        migrations.CreateModel(
            name='AchievementTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_links', to='api.achievement')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievement_links', to='api.tag')),
            ],
            options={
                'unique_together': {('achievement', 'tag')},
            },
        ),
        migrations.AddField(
            model_name='achievement',
            name='tags',
            field=models.ManyToManyField(related_name='achievements', through='api.AchievementTag', to='api.tag'),
        ),
    ]
