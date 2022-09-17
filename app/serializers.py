from rest_framework import serializers
from app.models import *

class ProductSerializer(serializers.ModelSerializer):
    # Получение нормального вывода названия обследования, а не просто id ключа
    class Meta:
        model = Product
        fields = [
            'id',
            'product_type_key',
            'photo',
            'is_exists',
            'slug_product',
        ]

class ProductTypeSerializer(serializers.ModelSerializer):
    # Получение нормального вывода названия обследования, а не просто id ключа
    class Meta:
        model = ProductType
        fields = [
            'id',
            'name_of_type',
        ]