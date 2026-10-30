from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    ROLE_CHOICE=(
        
        ('ADMIN','Admin'),
        ('CUSTOMER','Customer'),
        ('DELIVERY','Delivery_Partner'),        
        
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=30,choices=ROLE_CHOICE)
    
    
class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    
class FoodItem(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    
class Order(models.Model):
    STATUS=(
        ('PLACED','Placed'),
        ('PREPARING','Preparing'),
        ('OUT','Out_delivery'),
        ('DELIVERD','Deliverd'),    
    )
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='customer')
    delivery_partner=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='delivery')
    items=models.ManyToManyField(FoodItem)
    status=models.CharField(max_length=20,default="PLACED",choices=STATUS)
    