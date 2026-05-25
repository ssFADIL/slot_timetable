from django.shortcuts import render
from .models import Timetable

def timetable_view(request):
    timetable = Timetable.objects.all()

    return render(request, 'timetable.html', {
        'timetable': timetable
    })