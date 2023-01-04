from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    lesson_type = models.CharField(max_length=30)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

class Lecture(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    index = models.IntegerField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class Test(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    output_generator = models.CharField(max_length=255)
    no_test_cases = models.IntegerField()
    index = models.IntegerField()
    save_sources = models.IntegerField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class Input(models.Model):
    data_type = models.CharField(max_length=30)
    values = models.CharField(max_length=255)
    name = models.CharField(max_length=30)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)