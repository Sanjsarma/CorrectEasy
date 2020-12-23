from __future__ import unicode_literals

from django.db import models

# Create your models here.
class history(models.Model):
    rno=models.IntegerField(default=0)
    marks=models.IntegerField(default=0)
    name=models.CharField(max_length=100,default='')
    clname=models.CharField(max_length=100,default='')
    imageurl=models.CharField(max_length=100,default='')
    tmarks=models.IntegerField(default=0)

class Totalmarks(models.Model):
    rno=models.IntegerField(default=0)
    totmarks=models.IntegerField(default=0)
    name=models.CharField(max_length=100,default='')
    clname=models.CharField(max_length=100,default='')


