from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from .managers import UserManager
from django.utils import timezone
    
class User(AbstractUser):
    username = None # override user from base user class / delete username
    id = models.CharField(primary_key=True, max_length=50)
    email = models.EmailField(verbose_name='Email', null=True, unique=True, max_length=100, db_index=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    objects = UserManager() # custom manager create above 

    USERNAME_FIELD = 'email' # make the user log in with the email
    REQUIRED_FIELDS = []


    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
    
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name



class Company(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    
    pass

class employee(models.Model):
    pass