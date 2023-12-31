from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000,blank=False)
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    brand = models.CharField(max_length=200,default="",blank=False)
    image = models.ImageField(upload_to='images/%y/%m/%d',null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # number of items available
    stock = models.IntegerField(default=0)
    # time that are created
    createAt = models.DateTimeField(auto_created=True)
    # availability متاح 
    availabe = models.BooleanField(default=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    
