from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=254, verbose_name='email')

    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='phone', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='country', **NULLABLE)

    is_active = models.BooleanField(default=False, verbose_name='status of activation')
    verification_code = models.CharField(max_length=100, verbose_name='verification code', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
