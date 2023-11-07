from rest_framework.permissions import BasePermission


class IsOwnerOrReadonly(BasePermission):
    # имеет ли право создатель на просмотр ресурсов
    # def has_permission(self, request, view):
    # по умолчанию возвращает True, поэтому менять не надо

    # проверяет права на конкретный объект
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user == obj.user
