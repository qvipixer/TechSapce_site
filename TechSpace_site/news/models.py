import datetime

from django.db import models
from django.shortcuts import reverse
from home.models import Tags, SubCategory, Category


# Create your models here.

class Article(models.Model):  # Модель статей
    title = models.CharField('Заголовок', max_length=128, default='не определено')
    category = models.ForeignKey(Category, related_name='article', on_delete=models.CASCADE, blank=True)
    subcategory = models.ForeignKey(SubCategory, related_name='article', on_delete=models.CASCADE, blank=True)
    create = models.DateField('Дата добавления', default=datetime.date.today)
    update = models.DateTimeField('Дата редактирования', auto_now=True)
    description = models.TextField('Описание')
    tags = models.ManyToManyField(Tags, blank=True, related_name='article')
    author = models.CharField('Автор', max_length=64, default='не определено')
    image = models.ImageField('Эскиз', upload_to='article/%Y/%m/%d', blank=True, default='null.jpg')
    slug = models.SlugField('URL', max_length=200, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
