"""
Defining Database Schema
"""
from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class Paper(models.Model):
    uid = models.CharField(max_length=30)
    title = models.TextField()
    abstract = models.TextField()
    fl_subject = models.TextField()
    sl_subject = models.TextField()

    def __str__(self) -> str:
        return self.title


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return new user"""
        if not email:
            raise ValueError('User Must Have Error')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'