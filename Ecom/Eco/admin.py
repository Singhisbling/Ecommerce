from django.contrib import admin
from .models import Product,MyCart,Order,Address
# Register your models here.
admin.site.register(Product)
admin.site.register(MyCart)
admin.site.register(Address)
admin.site.register(Order)