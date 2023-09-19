from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings

import csv


def index(request):
    return redirect(reverse('bus_stations'))


with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
    CONTENT = list(csv.DictReader(file))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, per_page=10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': paginator.get_page(page_number),
        'page': page,
    }
    return render(request, 'stations/index.html', context)
