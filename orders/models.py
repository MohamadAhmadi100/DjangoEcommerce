from django.db import models
from django.conf import settings
from shop.models import Product


class Order(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='کاربر',
                                related_name='user_order')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, verbose_name='پرداخت شده')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    def __str__(self):
        return f"{self.user} - {self.id} - {self.created.date()}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', verbose_name='سفارش', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول', related_name='order_product')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    quantity = models.SmallIntegerField(verbose_name='تعداد')

    class Meta:
        verbose_name = 'جزئیات سفارش'
        verbose_name_plural = 'جزئیات سفارش'

    def __str__(self):
        return f"{self.id} - {self.product}"

    def get_cost(self):
        return self.price * self.quantity
