from django.contrib import admin

# Register your models here.

from .models import Articles, Category


class ArticleAdmin(admin.ModelAdmin):


    list_display = ('title', 'created', 'user', 'category', 'views')


    prepopulated_fields = {'slug': ('title', )}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


    prepopulated_fields = {'slug': ('title', )}



admin.site.register(Articles, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)