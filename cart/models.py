from django.db import models
from product.models import Product
from django.contrib.auth.models import User


class Cart(models.Model):
    """ Product Category Model Class """
    # product PK Refrence as FK because cart can have multiple products for different user
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    """ 
        Return a object representation string. Model Object PK to Cart Quantity. 
        example Cart Object (1) to 1/2
    """
    def __str__(self):
        return str(self.quantity)
