from statistics import mode
from django.db import models

class ProductType(models.Model):
    name_of_type = models.CharField(max_length=50, verbose_name='Название типа консоли')

    def __str__(self):
        return f"{self.name_of_type}"

    class Meta:
        verbose_name = 'Тип консолей'
        verbose_name_plural = 'Типы консолей'


class Product(models.Model):
    product_type_key = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='К какому типу относится')
    photo = models.ImageField(
        # upload_to='media/',
        verbose_name='Фото'
    )
    is_exists = models.BooleanField(
        default=False,
        verbose_name='Есть ли в наличии'
    )
    slug_product = models.CharField(max_length=200, verbose_name='Ссылка на категорию')


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.product_type_key}"