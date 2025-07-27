from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import CustomUserMnager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    avatar = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    birthday = models.DateField(null=True, blank=True)  # <-- добавили дату рождения

    objects = CustomUserMnager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email or ""
