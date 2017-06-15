from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from base.models import Menu
from base.serializers import MenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

