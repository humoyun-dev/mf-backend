from django.db import models
from users.models import CustomUser


class Seller(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=255)
    id_number_of_passport = models.CharField(max_length=9, default="AD0000000")
    profile_picture = models.ImageField(upload_to='sellers-profiles/', blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True,)

    def __str__(self):
        return self.phone_number

