from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, Favorite
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(creator=self.request.user)  # исключаем чужие черновики
        else:
            queryset = queryset.exclude(status='DRAFT')  # исключаем все черновики
        return queryset

    @action(methods=['post'], detail=True)
    def add_favorites(self, request):
        try:
            user = request.user
            adv_title = request.data.get('title')
            if not adv_title:
                return Response({'error': "Title is required"}, status=HTTP_400_BAD_REQUEST)

            adv_description = request.data.get('description', '')
            if adv_description:
                adv = Advertisement.objects.get(title=adv_title, description=adv_description)
            else:
                adv = Advertisement.objects.get(title=adv_title)

            Favorite.objects.create(user=user, advertisement=adv)
            return Response({'success': 'Advertisement added to favorites'}, status=HTTP_200_OK)

        except Advertisement.DoesNotExist:
            return Response({'error': "Advertisement with this title or description doesn't exist"},
                            status=HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error': error}, status=HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def get_favorites(self, request):
        user = request.user
        fav_adv = Favorite.objects.filter(user=user)
        if not fav_adv:
            return Response({'result': "You don't have any favorite advertisements"})
        serializer = self.get_serializer(fav_adv, many=True)
        return Response(serializer.data)