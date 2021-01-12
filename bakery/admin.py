from django.contrib import admin

from .models import User, Product, Order, OrderItem, ItemQuantity

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "category", "ingredients")

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "authority")

admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ItemQuantity)

