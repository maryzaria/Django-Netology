from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from router.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=10)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']

    # если хотим создать метод валидации какого-либо поля, пишем validate_<название поля>
    def validate_text(self, value):
        if 'text' in value:
            raise ValidationError('Вы использовали запрещенное слово')
        return value

    # если хотим валидировать сразу несколько полей
    # def validate(self, attrs):
    #     if 'hello' in attrs['text'] or attrs['user'].id == 1:
    #         raise ValidationError('Что-то пошло не так')
    #     return attrs

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)