from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    Student_email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_name
