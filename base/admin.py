from django.contrib import admin

# Register your models here.

from .models import Menu



class BaseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Дополнительная информация', {'fields': ['link', 'css_class']}),
    ]
    list_display = ('name', 'link', 'css_class')


admin.site.register(Menu, BaseAdmin)