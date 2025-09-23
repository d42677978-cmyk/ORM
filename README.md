# Ex02 Django ORM Web Application
## Date:17.09.25 

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).




## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from.models import car,carAdmin
admin.site.register(car,carAdmin)

models.py
from django.db import models
from django.contrib import admin
class car (models.Model):
    car_name=models.CharField(max_length=20)
    dom=models.DateField()
    color=models.CharField(max_length=20)
    engine_type=models.CharField(max_length=20)
    company=models.CharField(max_length=20)

class carAdmin(admin.ModelAdmin):
    list_display=('car_name','dom','color','engine_type','company')


```


## OUTPUT
![alt text](<Screenshots/Screenshot 2025-09-23 093044.png>)




## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
