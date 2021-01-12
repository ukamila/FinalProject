from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    TYPES = [
        ('CUSTOMER', 'Customer'),
        ('STAFF', 'Staff')
    ]
    authority = models.CharField(choices=TYPES, max_length=25, blank=True, verbose_name="Authority", null=True)

class Product(models.Model):
    ACTIVE_CATEGORIES = [
        ('CAKES', 'Cakes'),
        ('PASTRIES', 'Pastries'),
        ('COOKIES', 'Cookies'),
        ('DRINKS', 'Drinks')
    ]
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=600, blank=True)
    price = models.IntegerField()  
    category = models.CharField(choices=ACTIVE_CATEGORIES, blank=True, verbose_name="Category", max_length=200, null=True)
    image = models.URLField(max_length = 250, null=True)
    ingredients = models.CharField(max_length=300, blank=True)
    size = models.CharField(max_length=64, null=True)
    
    def __str__(self):
        return f"{self.title}" 

class OrderItem(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="orderitemproduct")
    quantity = models.IntegerField()
    price = models.IntegerField()

class ItemQuantity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="product")
    quantity = models.IntegerField()

class Order(models.Model):
    buyer =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="buyer")
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    location = models.CharField(max_length=100)
    total_price = models.IntegerField()
    items = models.ManyToManyField('ItemQuantity', blank=True, related_name="items_to_order")
    active = models.BooleanField(default=True)

