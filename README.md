# Ex02 Time Table
## Date:

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create a static folder and inert HTML code.

### STEP 3
Create a simple table using ```<table>``` tag in html.

### STEP 4
Add header row using ```<th>``` tag.

### STEP 5
Add your timetable using ```<td>``` tag.

### STEP 6
Execute the program using runserver command.

## PROGRAM:
modols.py
```
from django.db import models

class Timetable(models.Model):
    day = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day} - {self.subject}"
```
admin.py
```
from django.contrib import admin
from .models import Timetable

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('day', 'subject', 'teacher', 'start_time', 'end_time')
```
apps.py
```
from django.apps import AppConfig


class TryappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tryapp'
```

## OUTPUT:

![alt text](<Screenshot 2026-05-25 094838.png>)

## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
