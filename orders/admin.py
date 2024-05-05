from django.contrib import admin
from orders.models import Order, ProductOrder

class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductOrderInline]
    list_display = ("pk", 'name', 'phone_number', 'owner')
    list_filter = ('owner',)
    search_fields = ('name', 'phone_number',)



admin.site.register(Order, OrderAdmin)
# admin.site.register(ProductOrder)