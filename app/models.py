from django.db import models

# Create your models here.
class course(models.Model):
    name = models.CharField(max_length=32)

class student(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    courses = models.ManyToManyField(course,blank=True,related_name="students")

    def __str__(self):
        return self.name

