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

class PeriodMaster(models.Model):
    periodId = models.CharField(default='', max_length=10000)
    periodDate = models.CharField(default='', max_length=10000)
    periodCode = models.CharField(default='', max_length=10000)

class RecordDetail(models.Model):
    recordId = models.CharField(default='', max_length=10)
    recordNumber = models.CharField(default='', max_length=10)
    openTime = models.CharField(default='',max_length=10)
    periodNumber = models.CharField(default='',max_length=100)
    price = models.CharField(default='',max_length=100)
    colorId = models.CharField(default='', max_length=10)
    numberId = models.CharField(default='', max_length=10)
