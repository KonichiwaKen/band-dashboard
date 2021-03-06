from ConfigParser import ConfigParser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


class AccountManager(BaseUserManager):
    config_parser = ConfigParser()
    config_parser.read("config.cfg")

    def create_user(self, email, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('first_name') or not kwargs.get('last_name'):
            raise ValueError('Users must have a valid first name and last name.')

        account = self.model(
            email=self.normalize_email(email),
            first_name=kwargs.get('first_name'),
            last_name=kwargs.get('last_name'))

        default_password = self.config_parser.get('Accounts', 'DefaultPassword')
        account.set_password(default_password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_registered = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name
