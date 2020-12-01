import datetime

from django.db import models
from django.shortcuts import reverse
from home.models import Tags, SubCategory, Category


# Create your models here.
class Tasks(models.Model):  # Модель задач
    title = models.CharField('Название', max_length=50, default='не определено')
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='tasks', on_delete=models.CASCADE)
    progress = models.CharField('Прогрес выполнения', max_length=255, default='')
    status = models.BooleanField('Статус', default=False)
    description = models.TextField('Полное описание')
    tags = models.ManyToManyField(Tags, blank=True, related_name='tasks')
    create = models.DateField('Дата добавления', default=datetime.date.today)
    update = models.DateTimeField('Дата редактирования', auto_now=True)
    slug = models.SlugField('URL', max_length=200, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'
