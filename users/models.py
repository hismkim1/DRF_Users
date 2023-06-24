
# Create your models here.

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=70)
    username = models.CharField(max_length=70)


def __str__(self):
        return self.name


