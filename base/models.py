

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=30, default='#!')
    css_class = models.CharField(max_length=30, default='menu-item')

    def __str__(self):
        return self.name


class AbstractDateTimeMode(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


