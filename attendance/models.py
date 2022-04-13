from django.db import models

# Create your models here.

class Student(models.Model):
    """Students Records"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registeration_number = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.registeration_number}"

class Unit(models.Model):
    """Units Details"""
    unit_code = models.CharField(max_length=50, primary_key=True)
    unit_name = models.CharField(max_length=150)

    def __str__(self):
        return self.unit_code + ": " + self.unit_name


class Lecturer(models.Model):
    """Lecturer's Details"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Attendance(models.Model):
    """Attendance Details"""
    venue = models.CharField(max_length=100)
    time_of_lecture = models.DateTimeField(auto_now=False)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    
    def __str__(self):
        return f"Attendance for: {self.time_of_lecture}"



