from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50)
    number_credits = models.IntegerField()

    def __str__(self):
        #return u'{}'.format(self.name)
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject_student = models.ManyToManyField(Subject)