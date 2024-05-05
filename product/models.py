from django.db import models
from shop.models import Shop
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=455)
    enter_price = models.DecimalField(max_digits=10, decimal_places=2)
    out_price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    count = models.IntegerField(default=0)
    info = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="owned_products", default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop", default=1)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(blank=False, upload_to='product/images/')

    def image_url(self):
        return self.image.url

class Proporties(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="properties")
    feature = models.CharField(max_length=455)
    value = models.CharField(max_length=455)

    def __str__(self):
        return self.feature