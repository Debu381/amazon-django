from django.contrib import admin
from . models import Cart


""" 
    Cart Admin Class : To change the default behavior of Django Adminstration
"""
class CartAdmin(admin.ModelAdmin):
    #list_display is used to add columns of model attributes to Django adminstration table view of app model
    # product (product name), user (user's username) and status will displayed as table columns
    list_display = ['product', 'user', 'quantity']
    
    
"""
    Register App to Django Admin by passing model name as 1st parameter 
    admin.site.register(MODEL_NAME)    
    2nd paramter is option, if you want to change the default behavior of Django Admin then write a class and pass the class as 2nd parameter.
"""
admin.site.register(Cart, CartAdmin)

