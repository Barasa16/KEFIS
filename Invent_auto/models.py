from django.db import models

# Create your models here.
class Products(models.Model):
    Product_id = models.AutoField(primary_key=True)
    Serial_no = models.CharField(unique=True, max_length=16)
    Name = models.CharField(max_length=100)
    Metric = models.CharField(max_length=20, null=True)
    Items = models.IntegerField()
    Min_no = models.IntegerField()
    Order = models.Foreignkey(Orders, on_delete=models.CASCADE, related_name="Order")


class Retailers(models.Model):
    Store_id = models.AutoField(primary_key=True)
    Store_name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Contact = models.CharField(max_length=20, null=True)
    Telephone = models.IntegerField()


class Orders(models.Model):
    Order_id = models.AutoField(primary_key=True)
    Store = models.ForeignKey(Retailers, on_delete=models.CASCADE, related_name="Store")
    located = models.ForeignKey(
        Retailers, on_delete=models.CASCADE, related_name="located"
    )
    Serial = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="Serial"
    )
    Product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="Product"
    )
    Quantity = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="Quantity"
    )
    Processed = models.BooleanField(default=False)
