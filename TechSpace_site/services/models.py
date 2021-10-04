from django.db import models
from django.shortcuts import reverse


# Create your models here.

class Services_category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Категорию услуг"
        verbose_name_plural = "Категории услуг"

    def __str__(self):
        return self.name


class Services_subCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    category = models.ForeignKey(
        Services_category, related_name="subcategory", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Подкатегорию услуг"
        verbose_name_plural = "Подкатегории услуг"

    def __str__(self):
        return self.name
