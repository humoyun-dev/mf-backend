from django.db import models
import random
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Status(models.Model):
    status_name = models.CharField(max_length=255, unique=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.status_name}"


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The phone number must be set.')

        user = self.model(phone_number=phone_number, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password=password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(unique=True, max_length=12)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sms_verify = models.CharField(max_length=6, default="000000")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    profile_image = models.ImageField(upload_to='user/profile/image', blank=True, null=True)
    last_token_exchange = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.sms_verify = ''.join(random.choices('0123456789', k=6))
        super().save(*args, **kwargs)

    def generate_verification_code(self):
        return ''.join(random.choices('0123456789', k=6))

    def __str__(self):
        return str(self.phone_number)


@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        create_or_update_auth_token(instance)


def create_or_update_auth_token(user_instance):
    token, created = Token.objects.get_or_create(user=user_instance)
    user_instance.last_token_exchange = timezone.now()
    user_instance.save()
