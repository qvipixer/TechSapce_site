import datetime

from django.db import models
from django.shortcuts import reverse
from home.models import Tags, SubCategory, Category


# Create your models here.

class Project(models.Model):  # Модель проектов
    title = models.CharField('Название проекта', max_length=14)
    category = models.ForeignKey(Category, related_name='project', on_delete=models.CASCADE)
    category_sub = models.ForeignKey(SubCategory, related_name='project', on_delete=models.CASCADE)
    status = models.BooleanField('Статус', default=False)
    progress = models.CharField('Прогрес выполнения', max_length=255, default='')
    create = models.DateField('Дата добавления', default=datetime.date.today)
    update = models.DateTimeField('Дата редактирования', auto_now=True)
    description = models.TextField('Описание проекта')
    tags = models.ManyToManyField(Tags, blank=True, related_name='project')
    author = models.CharField('Автор проекта', max_length=64)
    image = models.ImageField('Эскиз', upload_to='project/%Y/%m/%d', blank=True, default='null.jpg')
    slug = models.SlugField('URL', max_length=200, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
