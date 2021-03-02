from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.core.validators import MinValueValidator

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, nick_name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Email address required')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, nick_name=nick_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create a superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users profile"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Get Full name of user"""
        return self.name

    def get_short_name(self):
        """Get short name of user"""
        return self.nick_name

    def __str__(self):
        """Return string representation of user"""
        return self.email


class Income(models.Model):
    """Income items"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    income_amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.00)])
    income_details = models.CharField(max_length=255, blank=True)
    date = models.DateField(blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        """Return model as string"""
        return self.income_amount


class Budget(models.Model):
     """Budget per expense tag type"""
     user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     expense_tag = models.CharField(max_length=30)
     budget_amount =  models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2, validators=[MinValueValidator(0.00)])
     
     def __str__(self):
        """Return model as string"""
        return self.expense_tag


class ExpenseItem(models.Model):
    """Expense items"""
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    expense_item = models.CharField(max_length=255)
    expense_amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.00)])
    expense_tag = models.ForeignKey(Budget, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        """Return model as string"""
        return self.expense_item