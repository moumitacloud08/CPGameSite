from django.db import models

# Create your models here.
class Panel(models.Model):
    userid = models.CharField(default='', max_length=10)
    color = models.CharField(default='',max_length=10)
    number = models.CharField(default='',max_length=2)
    contractPoint = models.CharField(default='',max_length=10)
    point = models.CharField(default='',max_length=10)
    period = models.CharField(default='',max_length=10)
    created = models.DateTimeField(auto_now_add = True)

class NumberMaster(models.Model):
    numberId = models.CharField(default='', max_length=10)
    numberDesc = models.CharField(default='',max_length=10)

class ColorMaster(models.Model):
    colorId = models.CharField(default='', max_length=10)
    colorCode = models.CharField(default='', max_length=10)
    colorDesc = models.CharField(default='',max_length=10)
