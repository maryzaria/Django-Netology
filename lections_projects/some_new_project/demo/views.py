from random import choice

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.shortcuts import render

from demo.models import Car, Person, Order


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


def summarize(request, op1, op2):
    result = op1 + op2
    return HttpResponse(f'Sum = {result}')


CONTENT = [str(i) for i in range(10000)]


def pagi(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, per_page=10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'pagi.html', context)


def create_car(request):
    # чтобы создать запись в БД, надо сделать следующие шаги:
    # создаем нужную запись
    car = Car(
        brand=choice(['A1', 'A2']),
        model=choice(['B1', 'B2']),
        color=choice(['black', 'red', 'white']))
    # сохраняем объект, после чего запись появится в БД
    car.save()
    return HttpResponse(f'Все получилось! Новая машина: {car.brand}, {car.model}')


# извлекаем данные из БД
def list_car(request):
    # car_obj = Car.objects.all() - all - все записи
    # задать условия фильтрации:
    car_obj = Car.objects.filter(brand='A1')
    #  модификаторы
    car_obj = Car.objects.filter(brand__contains='2')
    cars = [f'{car.id}: {car.brand}, {car.model}: {car.color} | {car.owners.count()}' for car in car_obj]
    return HttpResponse('<br>'.join(cars))


def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        # Person(name='Pers', car=car).save()  # первый способ
        Person.objects.create(name='Pers', car=car)  # второй способ
    return HttpResponse('Все получилось')


def list_pers(request):
    pers_obj = Person.objects.all()
    people = [f'{pers.name} - {pers.car}' for pers in pers_obj]
    return HttpResponse('<br>'.join(people))


def list_orders(request):
    orders = Order.objects.filter(positions__product__price__gte=600)
    context = {'orders': orders}
    return render(request, 'orders.html', context)