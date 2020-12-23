from __future__ import unicode_literals

from django.db import models

# Create your models here.
class history(models.Model):
    rno=models.IntegerField(default=0)
    marks=models.IntegerField(default=0)