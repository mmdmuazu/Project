from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    search_fields = ('name',)
    list_filter = ('available',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product', 'quantity', 'total_price', 'paid', 'created_at')
    search_fields = ('customer_name', 'product__name')
    list_filter = ('paid', 'created_at')
