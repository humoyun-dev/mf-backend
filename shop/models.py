from django.db import models
from users.models import CustomUser



class Shop(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='shops/images/', blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_shops', default=1)


    def __str__(self):
        return self.name