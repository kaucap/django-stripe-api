from django.db import models
from django.urls import reverse


class Item(models.Model):
    CURRENCY = (
        ('ru', 'RUB'),
        ('us', 'USD')
    )
    name = models.CharField(max_length=200, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.IntegerField(default=0, verbose_name='Цена')
    currency = models.CharField(max_length=2, choices=CURRENCY, default='ru')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.pk)])
