from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    address = models.TextField()

    def __str__(self):
        return str(self.id)
    

class OrderDetails(models.Model):
    """ related_name is used to get order Details when order calling object  """
    """ how to use: CurrentObject.related_name.all() in view  """
    """ how to use: CurrentObject.related_name.all in template  """
    """ example: order.orders.all() or order.orders.all  """
    
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.orders)




