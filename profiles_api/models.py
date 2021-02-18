from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, full_name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Email address required')

        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(slef, email, full_name, password):
        """Create a superuser with given details"""
        user = self.create_user(email, full_name, password)

        user.issuperuser = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users profile"""
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Get Full name of user"""
        return self.full_name

    def get_short_name(self):
        """Get short name of user"""
        return self.nick_name

    def __str__(self):
        """Return string representation of user"""
        return self.email
