import datetime

from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Tasks(models.Model):  # Модель задач
    title = models.CharField('Название', max_length=50, default='не определено')
    #tags = models.ManyToManyField('Tags', blank=True, related_name='task')
    progress = models.CharField('Прогрес выполнения', max_length=255, default='')
    status = models.BooleanField('Статус', default=False)
    descriptions = models.TextField('Описание')
    dataTime = models.DateField('Дата добавления', default=datetime.date.today)
    slug =  models.SlugField('URL', max_length=200, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'