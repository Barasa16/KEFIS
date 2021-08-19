from django.shortcuts import render

# Create your views here.
from Invent_auto.models import Products, Retailers, Orders
from rest_framework import viewsets
from rest_framework import permissions
from Invent_auto.Serializers import (
    ProductsSerializer,
    RetailersSerializer,
    OrdersSerializer,
)


class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def Sale


class RetailersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Retailers.objects.all()
    serializer_class = RetailersSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrdersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Orders.objects.all()
    queryset = Orders.filter()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]
