from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.db import models

from petstagram.accounts.managers import AppUserManager
from petstagram.accounts.validators import name_contains_only_letters


# UserModel = get_user_model()


class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = AppUserManager()


class Profile(models.Model):
    MAX_NAME_LEN = 30
    MIN_NAME_LEN = 2
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    )

    first_name = models.CharField(
        max_length=MAX_NAME_LEN,
        validators=[validators.MinLengthValidator(MIN_NAME_LEN), name_contains_only_letters]
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
        validators=[validators.MinLengthValidator(MIN_NAME_LEN), name_contains_only_letters]
    )

    profile_picture = models.URLField()
    gender = models.CharField(
        choices=CHOICES
    )

    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.user.username
