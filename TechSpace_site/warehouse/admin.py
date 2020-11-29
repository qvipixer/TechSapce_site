from django.contrib import admin
from .models import Thing


# Register your models here.

class ThingAdmin(admin.ModelAdmin):
    # list_display = ['title', 'progress', 'status']  # Список отображаемых полей в адмике
    # list_filter = ['progress', 'status']  # Список фильтруемы полей в адмике
    # list_editable = ['progress', 'status']  # список полей, которые можно будет редактировать на странице списка
    prepopulated_fields = {'slug': ('name',)}  # Генерация URL из названия

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


admin.site.register(Thing, ThingAdmin)  # Подлючаем к админке Задачи
