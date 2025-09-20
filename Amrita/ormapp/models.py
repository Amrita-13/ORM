from django.db import models
from django.contrib import admin
class owner(models.Model):
    Model=models.CharField(max_length=10)
    car_no=models.IntegerField(primary_key=True)
    quality= models.CharField(max_length=10)
    year_prod=models.IntegerField()
    colour=models.CharField(max_length=10)
class ownerAdmin(admin.ModelAdmin):
    list_display=["model","car_no","quality","year_prod","colour"]


