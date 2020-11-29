import datetime

from django.db import models
from django.shortcuts import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    category = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегорию'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
