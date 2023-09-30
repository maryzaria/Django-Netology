from random import choice

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.shortcuts import render

from demo.models import Order


def list_orders(request):
    orders = Order.objects.filter(positions__product__price__gte=600)
    context = {'orders': orders}
    return render(request, 'orders.html', context)