import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().time().strftime('%H:%M:%S')

    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    dir_list = ', '.join(os.listdir())

    msg = f'Содержимое рабочей директории: {dir_list}'
    return HttpResponse(msg)
