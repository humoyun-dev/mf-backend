from django.contrib import admin
from .models import Shop

class CustomShopAdmin(admin.ModelAdmin):
    model = Shop
    list_display = ('id', 'name')

admin.site.register(Shop, CustomShopAdmin)