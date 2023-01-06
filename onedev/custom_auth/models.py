from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.uploads import get_avatar_path


class CustomUser(AbstractUser):
    avatar = models.ImageField(
        upload_to=get_avatar_path,
        blank=True,
        null=True
    )
    email = models.EmailField(
        unique=True
    )
    bio = models.TextField(
        max_length=2048,
        blank=True,
        null=True
    )
    birth_date = models.DateField()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "birth_date"]

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
