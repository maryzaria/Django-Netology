import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from demo.models import Message


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user('admin')


@pytest.fixture
def message_factory():
    def factory(*args, **kwargs):
        # мы нигде не заполняем поля, model_bakery берет это на себя
        return baker.make(Message, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_messages(client, user, message_factory):
    # Arrange - подготовка данных
    # client = APIClient() - вместо этого используем фикстуру client
    # User.objects.create_user('admin') -  - вместо этого используем фикстуру user
    # Message.objects.create(user_id=user.id, text='test')
    messages = message_factory(_quantity=10)

    # Act - вызов функционала
    response = client.get('/messages/')

    # Assert - проверка, корректно ли выполнено действие
    assert response.status_code == 200
    # Проверяем не только статус возврата, но и содержимое ответа
    data = response.json()
    assert len(data) == len(messages)
    # assert data[0]['text'] == 'test'
    for i, m in enumerate(data):
        assert m['text'] == messages[i].text


@pytest.mark.django_db
def test_create_message(client, user):
    # client = APIClient() - вместо этого используем фикстуру client
    # User.objects.create_user('admin') -  - вместо этого используем фикстуру user
    count = Message.objects.count()

    response = client.post('/messages/', data={'user': user.id, 'text': 'test text'})  # format='json' больше не указываем, т.к. сделали это в settings.py

    assert response.status_code == 201
    assert Message.objects.count() == count + 1