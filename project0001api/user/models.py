from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """Class to work with User Model"""

    def create_user(self, email, username, password):
        """Create new user"""

        #check if email is empty
        if not email:
            raise ValueError('Can not be empty.')
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
        user.is_admin=True  
        user.is_superuser=True
        user.is_staff=True
        #save object to DB
        user.save(using=self._db)

        return user

        
class User(AbstractBaseUser):
    """ Represents users profile in system """
    """ Model's fields"""
    GENDER=(
        ('male','male'),
        ('female', 'female')
    )
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)#!Required
    username                = models.CharField(max_length=30, unique=True)#!Required
    avatar                  = models.ImageField(upload_to="user/avatar/", blank=True, null=True)
    bio                     = models.TextField(blank=True, null=True)
    birthday                = models.DateField(blank=True, null=True)
    first_login             = models.DateTimeField(blank=True,null=True)
    last_login              = models.DateTimeField(blank=True,null=True)
    gender                  = models.CharField(max_length=6,choices=GENDER, default='male')
    badges                  = models.ManyToManyField('Badge',related_name='users',blank=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

class Badge(models.Model):
    """User achivments in images form"""
    badge_name                 =models.CharField(max_length=20)            #text representation
    badge_image                =models.ImageField(upload_to="badges/",verbose_name='Badge')     #image representation

    def __str__(self):
        return self.badge_name