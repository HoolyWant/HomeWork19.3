from django.contrib import admin
from shop.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'buy_cost', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('product_name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
