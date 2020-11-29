from django.contrib import admin
from .models import Category, SubCategory, Tags


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    #    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    #    list_display = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(SubCategory, SubCategoryAdmin)


class TagsAdmin(admin.ModelAdmin):
    #    list_display = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tags, TagsAdmin)
