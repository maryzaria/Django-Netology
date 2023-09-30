"""
URL configuration for some_new_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from demo.views import hello_view, summarize, pagi, create_car, list_car, create_person, list_pers, list_orders

# прописываем маршруты
# имя маршрута нужно, чтобы использовать его потом в коде


urlpatterns = [
    path('admin/', admin.site.urls),  # лучше писать / на конце, это надежнее
    path('', hello_view, name='hello'),
    path('orders/', list_orders)
]
