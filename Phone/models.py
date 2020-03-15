from django.db import models
from django.utils import timezone

# Create your models here.


class Text(models.Model):
    tid = models.IntegerField(default=0, primary_key=True)
    txt = models.CharField(max_length=20)

    def __str__(self):
        return self.txt


class Color(models.Model):
    cid = models.IntegerField(default=0, primary_key=True)
    color = models.CharField(max_length=7)
    access_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.color
