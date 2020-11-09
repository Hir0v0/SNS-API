from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models
from rest_framework import validators

class UserManager(BaseUserManager):
    """Class to work with User Model"""

    def create_user(self, email, username, password):
        """Create new user"""

        #check if email is empty
        if not email:
            raise ValueError('Can not be empty.')
        #normalize email
        email=self.normalize_email(email)
        #create a user
        user=self.model(email=email, username=username)
        #convert password into hash and seta as object password
        user.set_password(password)
        #save object to DB
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """Create new su"""

        #create new user profile
        user=self.create_user(email, username, password)
        #give created user su rights
        user.is_superuser=True
        user.is_staff=True
        #save object to DB
        user.save(using=self._db)

        return user

        
class User(AbstractBaseUser, PermissionsMixin):
    """ Represents users profile in system """
    """ Model's fields"""
    email=models.EmailField(
        unique=True,
        blank=False
        )
    username=models.CharField(
        db_index=True, 
        max_length=255,
        unique=True)
    """Fields nessesary for inheritance"""
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    object=UserManager()

    #Authorized with email
    USERNAME_FIELD='email'
    #Require fields
    REQUIRED_FIELDS=['username']

    """ Function Section"""
    def get_username(self):
        """Username getter"""
        return self.username

    def __str__(self):
        """Object to string convertation"""
        return self.email
