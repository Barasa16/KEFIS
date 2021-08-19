from django.shortcuts import render

# Create your views here.
from Retail.models import Products, Listing
from rest_framework import viewsets
from rest_framework import permissions
from Retail.Serializers import ProductsSerializer, ListingSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]
