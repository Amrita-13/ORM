from django.db import models
from django.contrib import admin
class Car(models.Model):
     car_model=models.CharField(max_length=10)
     plate_no=models.IntegerField(primary_key=True)
     car_color=models.CharField(max_length=10)
     price=models.IntegerField()
     Adharno=models.IntegerField()

class CarAdmin(admin.ModelAdmin):
     list_display=('car_model','plate_no','car_color','price','Adharno')