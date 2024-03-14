from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Employee)
admin.site.register(Type)
admin.site.register(Customer)
admin.site.register(InventoryStock)
admin.site.register(ReceiveOrder)
admin.site.register(ReceiveDetail)
admin.site.register(SendOrder)