from django.contrib import admin
from .models import Category, Product, File

# Register your models here.


@admin.register(Category)    # this is enough for register models in admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_enable', 'created_time', 'parent']
    list_filter = ['parent', 'is_enable']
    search_fields = ['title']


# this is use for display  relation in model
class FileInLineAdmin(admin.StackedInline):
    model = File
    fields = ['id', 'title', 'file_type', 'file', 'is_enable']
    extra = 0     # for no display extra fields or blank fields


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_enable', 'created_time']
    list_filter = ['is_enable']
    filter_horizontal = ['categories']
    search_fields = ['title']
    inlines = [FileInLineAdmin]

