from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from .models import Adv
from .permissions import IsOwnerOrReadonly
from .serializers import AdvSerializer


class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadonly]
    throttle_classes = [AnonRateThrottle]  # если общие настройки в REST_FRAMEWORK['DEFAULT_THROTTLE_CLASSES'] отключены общие настройки

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

