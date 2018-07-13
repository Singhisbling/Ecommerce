from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Product(models.Model):

   productName = models.CharField(max_length = 50)
   price = models.IntegerField()
   left_quantity = models.IntegerField()
   specification = models.CharField(max_length = 50)
   image = models.ImageField(blank=True, null=True)


   def __str__(self):
      return self.productName
#bag to store items
class MyCart(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="mycart")
   productId=models.IntegerField(default=0)
   productName = models.CharField(max_length=50)
   price = models.IntegerField(default=0)
   quantity = models.IntegerField(default=1)
   image=models.ImageField(blank=True)
   def __str__(self):
      return str(self.user)



class Address(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name="address")
   first_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length=20)
   # email = models.EmailField(max_length=254)
   current_address = models.CharField(max_length=200,null=True)



   def __str__(self):
      return str(self.id)

class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='order')
   productName = models.CharField(max_length=30)
   total_price = models.IntegerField(default=0)
   quantity = models.IntegerField(default=0)
   image = models.ImageField(blank=True)
   address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True,related_name='address')

   def __str__(self):
      return self.productName