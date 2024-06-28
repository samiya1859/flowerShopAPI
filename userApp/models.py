from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser): 
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    shop_name = models.CharField(max_length=50,null=True,blank=True)
    is_customer=models.BooleanField(default=False)
    is_seller=models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    