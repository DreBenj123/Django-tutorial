from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, Customer, Order, OrderItem


def say_hello(request):
    queryset = Product.objects.filter(
        id__in=OrderItem.objects.values('product_id').distinct()).order_by("title")

    return render(request, 'hello.html', {"name": "Dre", "products": list(queryset)})
