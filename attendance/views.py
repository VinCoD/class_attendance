from django.shortcuts import render, HttpResponse
from .models import Attendance

# Create your views here.


def index(request):
    attendances = Attendance.objects.all()
    context = {"attendances":attendances}
    return render(request, 'attendance/index.html', context)