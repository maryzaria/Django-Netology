from django.urls import path

from .views import SensorAPIList, SensorRetrieveAPIView, MeasurementCreateAPIView

urlpatterns = {
    path('sensors/', SensorAPIList.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveAPIView.as_view()),
    path('measurements/', MeasurementCreateAPIView.as_view()),
}
