from django.contrib import admin
from .models import Project


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status',
                    'progress', 'author']  # Список отображаемых полей в адмике
    list_filter = ['status',
                   'progress', 'author']  # Список фильтруемы полей в адмике
    list_editable = ['status',
                     'progress']  # список полей, которые можно будет редактировать на странице списка

    prepopulated_fields = {'slug': ('title',)}  # Генерация URL из названия

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


admin.site.register(Project, ProjectAdmin)  # Подлючаем к админке Проекты
