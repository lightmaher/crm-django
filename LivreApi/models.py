from turtle import title
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_blocked = models.BooleanField(default=False , null =True)
    is_admin = models.BooleanField(default=False , null =True)

    user_gender=(("male","male") , ("female" , "female"))
    gender =models.CharField(max_length=6 , choices=user_gender)
    dob = models.DateField()

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=50 , null=True)
    description = models.T        