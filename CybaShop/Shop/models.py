from django.db import models

# Create your models here.

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
    quantity = models.IntegerField()
    phone = models.CharField()
    email = models.EmailField()
    address = models.CharField()
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)

    def __str__(self):
        return f"заказ {self.pk}"


class Category(models.Model):
    name = models.CharField()
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name
