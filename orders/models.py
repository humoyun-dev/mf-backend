from django.db import models
from product.models import Product
from sellers.models import Seller


class Order(models.Model):
    name = models.CharField(max_length=600, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    owner = models.ForeignKey(Seller, on_delete=models.CASCADE)

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        if self.name:
            return self.name
        elif self.phone_number:
            return self.phone_number
        else:
            return str(self.pk)


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders" )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.SmallIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="products", null=True)



    def __str__(self):
        return self.product.name
