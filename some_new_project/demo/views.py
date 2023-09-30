from random import choice

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.shortcuts import render

from demo.models import Order


# принимает запрос от пользователя и обрабатывает его
# какая функция вызывается при написании определенного адреса


def hello_view(request: HttpRequest) -> HttpResponse:
    # request.META.get('HTTP_REFERRER')
    # reverse('hello')  # использовали имя маршрута, чтобы при изменении маршрута все не сломалось
    # return HttpResponse('Hello!')
    context = {
        'test': 20,
        'data': [1, 5, 8],
        'val': 'hello'
    }
    return render(request, 'demo.html', context)


def list_orders(request):
    orders = Order.objects.filter(positions__product__price__gte=600)
    context = {'orders': orders}
    return render(request, 'orders.html', context)