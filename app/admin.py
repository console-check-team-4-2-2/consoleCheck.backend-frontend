from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product_type_key',
        'photo',
        'is_exists',
        'slug_product',
    ]

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name_of_type',
    ]
