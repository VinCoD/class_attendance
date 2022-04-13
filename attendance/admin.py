from django.contrib import admin
from .models import Student, Unit, Lecturer, Attendance
# Register your models here.


admin.site.register(Student)
admin.site.register(Unit)
admin.site.register(Lecturer)
admin.site.register(Attendance)

admin.site.site_header = "Class Attendance Management"