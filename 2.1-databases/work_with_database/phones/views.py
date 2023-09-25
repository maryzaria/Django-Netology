from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_id = request.GET.get('sort')
    phones = Phone.objects.all()
    context = {
        'phones': sort_phones(sort_id, phones)
    }
    return render(request, template, context)


def sort_phones(sort_id, phones):
    if sort_id == 'name':
        return phones.order_by('name')
    elif sort_id == 'min_price':
        return phones.order_by('price')
    elif sort_id == 'max_price':
        return phones.order_by('-price')
    return phones


def show_product(request, slug):
    template = 'product.html'
    item = Phone.objects.filter(slug__contains=slug)
    context = {'phone': item[0]}
    return render(request, template, context)
