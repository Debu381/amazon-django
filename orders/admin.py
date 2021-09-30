from django.contrib import admin
from orders import models as OrdersModels


admin.site.register(OrdersModels.Orders)
admin.site.register(OrdersModels.OrderDetails)