from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Goods)

admin.site.register(Category)

admin.site.register(Order)

admin.site.register(Basket)
