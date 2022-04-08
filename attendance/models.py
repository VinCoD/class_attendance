from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registeration_number = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.registeration_number

class Unit(models.Model):
    unit_code = models.CharField(max_length=50, primary_key=True)
    unit_name = models.CharField(max_length=150)

    def __str__(self):
        return self.unit_code + ": " + self.unit_name


class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(slef):
        return self.first_name + " " + self.last_name


class Attendance(models.Model):
    venue = models.CharField(max_length=100)
    time_of_lecture = models.DateTimeField(auto_now=False)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)



