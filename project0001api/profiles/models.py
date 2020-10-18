from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class ProfileManager(BaseUserManager):
    """Class to work with Profile Model"""

    def create_user(self, email, username, password):
        """Create new user Profile"""

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
        """Create new su Profile"""

        #create new user profile
        user=self.create_user(email, username, password)
        #give created user su rights
        user.is_superuser=True
        user.is_staff=True
        #save object to DB
        user.save(using=self._db)

        return user

        
class Profile(AbstractBaseUser, PermissionsMixin):
    """ Represents users profile in system """
    """ Model's fields"""
    email=models.EmailField(max_length=255, unique=True)
    username=models.CharField(max_length=255)
    """Fields nessesary for inheritance"""
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    object=ProfileManager()

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
