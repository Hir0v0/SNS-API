from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models

        
class Message():
    """ Represents messages in system """

    
    def __str__(self):
        """Object to string convertation"""
        return self.email
