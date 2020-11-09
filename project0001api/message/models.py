from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models

        
class Message():
    """ Represents messages in system """
    """ Model's fields"""
    email=models.EmailField(max_length=255, unique=True)
    username=models.CharField(max_length=255)
    """Fields nessesary for inheritance"""
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    
    def __str__(self):
        """Object to string convertation"""
        return self.email
