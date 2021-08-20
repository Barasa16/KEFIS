from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from Invent_auto.models import Products, Retailers, Orders
from Invent_auto.Serializers import (
    ProductsSerializer,
    RetailersSerializer,
    OrdersSerializer,
)

"""Create your views here."""


@api_view(["PUT"])
def apioverview(request):
    apiurls = {
        "sales": "/sales/<str:serial_no>/",
        "process": "/process/<str:store>/",
        "orders": "/order_list/<str:store>/",
        "products": "/products_list/",
        "retailers": "/retailers/",
    }
    return Response(apiurls)


""" The sale method allows me to edit the products table and change the number of items """


@api_view(["PUT"])
def sale(request, serial_no):
    sales = Products.objects.get(serial_no)
    serializer = ProductsSerializer(instance=sales, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


"""The process method allows us to edit and view the orders table  and post into the products table"""


@api_view(["pOST", "PUT", "GET"])
def process(request, store):
    if request.method == "PUT":
        dispatch = Orders.objects.all()
        serializer = OrdersSerializer(dispatch, many=False)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    if request.method == "GET":
        dispatch = Orders.objects.filter(store)
        serializer = ProductsSerializer(dispatch, data=request.data)

        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


"""The orderlist method allows us to view and post data into the orders table """


@api_view(["GET", "POST"])
def orderlist(request, store):
    if request.method == "GET":
        order = Orders.objects.filter(store)
        serializer = OrdersSerializer(order, many=False)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = OrdersSerializer(data=request.data)
        return Response(serializer.data)


"""The Productslist method aloows us to get and post data into the products table"""


@api_view(["GET", "POST"])
def productslist(request):
    product = Products.objects.all()

    if request.method == "GET":
        serializer = ProductsSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

    return Response(serializer.data)


"""The retailers method allows us to post and viw table data in the retailers table """


@api_view(["GET", "POST"])
def retailers(request):
    retailer = Retailers.objects.get(id)

    if request.method == "GET":
        serializer = ProductsSerializer(retailer, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = RetailersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

    return Response(serializer.data)
