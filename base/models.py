from django.db import models

# Create your models here.

from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=30, default='#!')
    css_class = models.CharField(max_length=30, default='menu-item')

    def __str__(self):
        return self.name