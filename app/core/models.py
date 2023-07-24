from django.db import models

# Create your models here.
from django.contrib.auth.models import (AbstractUser, BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        username = email
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email),username = username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser, PermissionsMixin):
    '''User in the system.'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []