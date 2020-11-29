import datetime

from django.db import models
from django.shortcuts import reverse
from home.models import Tags, SubCategory, Category


# Create your models here.


class Thing(models.Model):
    name = models.CharField('Название', max_length=128)
    author = models.CharField('Кто принёс', max_length=64)
    thumbnail = models.ImageField('Фото', upload_to='warehouse/%Y/%m/%d', blank=True, default='null.jpg')
    description_full = models.TextField('Описание')
    number = models.IntegerField('Колличество')
    create = models.DateField('Дата добавления', default=datetime.date.today)
    update = models.DateTimeField('Дата редактирования', auto_now=True)
    status = models.BooleanField('Статус', default=False)
    slug = models.SlugField('URL', max_length=200, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.slug

    class Meta:
        verbose_name = 'Что-то'
        verbose_name_plural = 'Что-ты'
