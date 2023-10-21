from rest_framework import generics

from .models import Measurement, Sensor
from .serializers import SensorDetailSerializer, SensorListSerializer, MeasurementListSerializer


class SensorAPIList(generics.ListCreateAPIView):  # получить список, создать датчик
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class SensorRetrieveAPIView(generics.RetrieveUpdateAPIView):  # Получить информацию по конкретному датчику, изменить датчик
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateAPIView(generics.ListCreateAPIView):  # Добавить измерение
    queryset = Measurement.objects.all()
    serializer_class = MeasurementListSerializer
