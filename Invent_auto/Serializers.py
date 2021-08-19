from Invent_auto.models import Products, Retailers, Orders
from rest_framework import serializers


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class RetailersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Retailers
        fields = "__all__"


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"
