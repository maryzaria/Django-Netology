from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    SORT_MAP = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }
    template = 'catalog.html'
    sort_id = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort_id:
        phones = phones.order_by(SORT_MAP.get(sort_id, ''))
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    item = Phone.objects.filter(slug__contains=slug)
    context = {'phone': item[0]}
    return render(request, template, context)
