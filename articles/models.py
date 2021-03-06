from django.contrib.auth.models import User
from django.db import models

from base.models import AbstractDateTimeMode
from heapbackend import settings
from tinymce_4.fields import TinyMCEModelField


class Articles(AbstractDateTimeMode):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True ,on_delete=models.SET_NULL )
    pretext = models.TextField(max_length=130)
    bodytext = TinyMCEModelField('Текст',blank=True, null=True)
    category = models.ForeignKey('Category')

    likes = models.IntegerField(blank=True, default=0,
                                verbose_name=("likes"))
    comments = models.IntegerField(blank=True, default=0,
                                verbose_name=("Комментарии"))
    views = models.IntegerField(blank=True, default=0,
                                verbose_name=("Просмотры"))
    imgUrl = models.ImageField(upload_to='img')


    @property
    def username(self):
        return self.user.username

    @property
    def categoryname(self):
        return self.category.title

class Category(AbstractDateTimeMode):
    title = models.CharField(max_length=100)
    slug = models.SlugField()




    def __str__(self):
        return self.title

