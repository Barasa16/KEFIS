from django.db import models

# Create your models here.


class Retailers(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=100, default="KEFIS")
    location = models.CharField(max_length=100, default="Kayole")
    contact = models.CharField(max_length=20, null=True, default="Wanjiru")
    telephone = models.CharField(max_length=10, default="0707....")

    def __str__(self):
        return self.location

    def __str__(self):
        return self.store_name


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    serial_no = models.CharField(unique=True, max_length=16, default="1122334455")
    name = models.CharField(max_length=100, default="Maize")
    metric = models.CharField(max_length=20, null=True, default="2Kgs")
    items = models.IntegerField(default=100)
    min_no = models.IntegerField(default=10)
    stock = models.IntegerField(default=100)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.metric

    def __str__(self):
        return self.items


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey(
        Retailers, on_delete=models.CASCADE, related_name="store", default="1"
    )
    located = models.ForeignKey(
        Retailers, on_delete=models.CASCADE, related_name="located", default=1
    )
    serial = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="serial", default="1122334455"
    )
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="product", default="maize"
    )
    quantity = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="quantity", default=100
    )
    processed = models.BooleanField(default=False)
