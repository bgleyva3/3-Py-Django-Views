from django.db import models

from lessons.models import Lesson

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    semester = models.IntegerField(default=1)

    lessons = models.ManyToManyField(Lesson, related_name='students')

    def __str__(self):
        return self.name