import datetime

from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Article(models.Model):  # Модель статей
    title = models.CharField('Заголовок', max_length=128, default='не определено')
    #tag = models.CharField('Тэг', max_length=255, default='')
    create = models.DateField('Дата добавления', default=datetime.date.today)
    update = models.DateTimeField('Дата редактирования', auto_now=True)
    short_description = models.TextField('Короткое описание')
    full_description = models.TextField('Полное описание')
    author = models.CharField('Автор', max_length=64, default='не определено')
    slug = models.SlugField('URL', max_length=200, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'