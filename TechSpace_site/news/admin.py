from django.contrib import admin
from .models import Article


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    # list_display = ['title', 'author', 'tag']  # Список отображаемых полей в адмике
    # list_filter = ['author', 'tag']  # Список фильтруемы полей в адмике
    prepopulated_fields = {'slug': ('title',)}  # Генерация URL из названия

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


admin.site.register(Article, ArticleAdmin)  # Подлючаем к админке Статьи
