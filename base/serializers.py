from rest_framework import serializers
from base.models import Menu

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('name', 'link', 'css_class')

