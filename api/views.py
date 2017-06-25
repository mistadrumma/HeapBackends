from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from articles.models import Articles
from api.serializers import ArticleSerializer, MenuSerializer
from base.models import Menu


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer




class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

