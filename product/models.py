from django.db import models
from django.db.models.base import Model


class ProductCategory(models.Model):
    """ Product Category Model Class """
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    
    """ 
        Return a object representation string. Model Object PK to Category Title. 
        example ProductCategory Object (1) to Shoes/Jeans/Tshirt 
    """
    def __str__(self):
        return str(self.name)


class Product(models.Model):
    """ Product Model Class """
    # ProductCategory PK Refrence as FK because ProductCategory can have multiple products
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField()
    status = models.BooleanField(default=True)
    
    """ 
        Return a object representation string. Model Object PK to Product. 
        example Product Object (1) to Cotton Jeans. 
    """ 
    def __str__(self):
        return str(self.name)
    