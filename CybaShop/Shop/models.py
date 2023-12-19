from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    is_published = models.BooleanField(default=False, null=True)
    image = models.ImageField(upload_to='photos', null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    basket = models.ManyToManyField('Basket')

    def __str__(self):
        return f"заказ {self.pk}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

class Basket(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()
    def __str__(self):
        return f"корзина пользователя {self.user.username}, товары: {self.good.name}, кол-во: {self.quantity}"

    def sum(self):
        return self.good.price * self.quantity
