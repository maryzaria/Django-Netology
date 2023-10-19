from django.urls import path

from .views import SensorAPIList, SensorRetrieveAPIView, MeasurementCreateAPIView

urlpatterns = {
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorAPIList.as_view()),
    # path('sensors/<int:pk>/', SensorAPIUpdate.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveAPIView.as_view()),
    path('measurements/', MeasurementCreateAPIView.as_view()),
}
