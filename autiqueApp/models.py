from django.db import models
from django.utils import timezone

#รับซื้อของเก่า
class Employee(models.Model):
    id = models.AutoField(primary_key=True,max_length=13, default="")
    userName = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    fullName = models.CharField(max_length=100, default="")
    address = models.TextField(default="")
    tell = models.CharField(max_length=10, default="")
    # Admin Added

class Customer(models.Model):
    id = models.AutoField(primary_key=True,max_length=13, default="")
    fullName = models.CharField(max_length=100, default="")
    address = models.TextField(default="")
    tell = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.fullName

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100, default="")
    rateReceive = models.IntegerField(default=0)
    rateSend = models.IntegerField(default=0)
    def __str__(self):
        return self.productName

class InventoryStock(models.Model):
    id = models.AutoField(primary_key=True)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, default=None)
    totalAmount = models.DecimalField(default=0.00)

class ReceiveOrder(models.Model):
    id = models.AutoField(primary_key=True)
    inv_id = models.ForeignKey(InventoryStock, on_delete=models.CASCADE, default=None)
    amount = models.IntegerField(default=0)
    total = models.DecimalField(default=0.00)
    date = models.DateTimeField(default=timezone.now)
    cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)

class SendOrder(models.Model):
    id = models.AutoField(primary_key=True)
    inv_id = models.ForeignKey(InventoryStock, on_delete=models.CASCADE, default=None)
    amount = models.IntegerField(default=0)
    total = models.DecimalField(default=0.00)
    date = models.DateTimeField(default=timezone.now)
    cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)