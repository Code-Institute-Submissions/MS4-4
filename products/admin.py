from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'description',
        'colour',
        'price',
        'image',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
