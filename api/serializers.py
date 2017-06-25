from rest_framework import serializers
from articles.models import Articles
from base.models import Menu


class ArticleSerializer(serializers.ModelSerializer):



    class Meta:
        model = Articles
        fields = ('id','title', 'slug', 'user', 'pretext','bodytext','category','created','likes','comments','views','imgUrl')

    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('name', 'link', 'css_class')
