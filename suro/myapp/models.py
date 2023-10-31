from django.db import models
from django.contrib import admin
class FootballPlayer (models.Model):
    p_id=models.CharField(max_length=20,help_text="ID")
    p_name=models.CharField(max_length=100)
    age=models.IntegerField()
    team_name=models.CharField(max_length=100)
class FootballPlayerAdmin(admin.ModelAdmin):
    list_display=('p_id','p_name','age','team_name')
