from django.contrib import admin
from . models import ProductCategory, Product


""" 
    ProductCategory Admin Class : To change the default behavior of Django Adminstration
"""
class ProductCategoryAdmin(admin.ModelAdmin):
    #list_display is used to add columns of model attributes to Django adminstration table view of app model
    # name and status will displayed as table columns
    list_display = ['name', 'status']

"""
    Register App to Django Admin by passing model name as 1st parameter 
    admin.site.register(MODEL_NAME)    
    2nd paramter is option, if you want to change the default behavior of Django Admin then write a class and pass the class as 2nd parameter.
"""
admin.site.register(ProductCategory, ProductCategoryAdmin)



""" 
    Product Admin Class : To change the default behavior of Django Adminstration
"""
class ProductAdmin(admin.ModelAdmin):
    #list_display is used to add columns of model attributes to Django adminstration table view of app model
    # name, product_category, price and status will displayed as table columns
    list_display = ['name', 'product_category', 'price', 'status']

"""
    Register App to Django Admin by passing model name as 1st parameter 
    admin.site.register(MODEL_NAME)    
    2nd paramter is option, if you want to change the default behavior of Django Admin then write a class and pass the class as 2nd parameter.
"""
admin.site.register(Product, ProductAdmin)