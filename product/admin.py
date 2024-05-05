from django.contrib import admin
from .models import Category, Product, ProductImage, Proporties


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
class ProportiesInline(admin.TabularInline):
    model = Proporties
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProportiesInline]
    list_display = ('name', 'enter_price', 'out_price', 'in_stock', 'count', 'category')
    list_filter = ('category', 'in_stock')
    search_fields = ('name', 'info')
