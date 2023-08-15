from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='продукт')
    description = models.CharField(max_length=150, verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category_name = models.CharField(max_length=150, verbose_name='категория')
    buy_cost = models.IntegerField(verbose_name='стоимость покупки')
    creation_date = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    last_change_date = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.product_name} {self.category_name} {self.buy_cost}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='категория')
    description = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
