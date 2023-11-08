from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )
    # данное поле будет вычисляться на основе некоторой функции get_is_favorite или прописать method_name=
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at', 'is_favourite')

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        request = self.context["request"]
        user = self.context["request"].user
        if request.method == 'POST' or data.get('status') == 'OPEN':
            if Advertisement.objects.filter(creator=user, status='OPEN').count() > 10:
                raise serializers.ValidationError('Превышен лимит объявлений: нельзя публиковать больше 10 объявлений')
        return data

    def get_is_favorite(self, obj):
        user = self.context['request'].user  # self.context - словарь из view функции
        if not user.is_authenticated:
            return False
        return obj.favorite_by.filter(id=user.id).exists()
