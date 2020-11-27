import datetime

from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Project(models.Model):  # Модель проектов
    title = models.CharField('Название проекта', max_length=128)
    type = models.CharField('Раздел', max_length=64)
    status = models.BooleanField('Статус', default=False)
    # tag = models.ManyToManyField('Tags', blank=True, related_name='project')
    # tagProject = models.CharField('Тэг', max_length=255, default='')
    progress = models.CharField('Прогрес выполнения', max_length=255, default='')
    create = models.DateField('Дата добавления', default=datetime.date.today)
    update = models.DateTimeField('Дата редактирования', auto_now=True)
    short_description = models.TextField('Короткое описание проекта', max_length=96)
    full_description = models.TextField('Полное описание проекта')
    author = models.CharField('Автор проекта', max_length=64)
    thumbnail = models.ImageField('Эскиз', upload_to='project/%Y/%m/%d', blank=True, default='null.jpg')
    slug = models.SlugField('URL', max_length=200, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'