from Retail.models import Products, Listing
from rest_framework import serializers


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ["id", "Serial_no", "Name", "Metric", "Items"]


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = ["id", "Serial_no", "Name", "Metric"]

