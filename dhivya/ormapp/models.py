from django.db import models
from django.contrib import admin
class car(models.Model):
    car_name=models.CharField(max_length=20)
    dom=models.DateField()
    color=models.CharField(max_length=20)
    engine_type=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
class carAdmin(admin.ModelAdmin):
    list_display=["name","dom","color","engine_type","company"]
