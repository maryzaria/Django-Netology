from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=50)


class Order(models.Model):
    products = models.ManyToManyField(Product, related_name='orders', through='OrderPosition')


# джанго создает автоматически промежуточную таблицу при реализации связи многие-к-многим, но можно описать ее самостоятельно
class OrderPosition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='positions')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions')
    quantity = models.IntegerField()