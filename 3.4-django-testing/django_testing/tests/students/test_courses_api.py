from random import choice

import pytest
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def course():
    return baker.make(Course)


@pytest.mark.django_db
def test_get_first_course(client, course):
    """Проверка получения первого курса"""
    response = client.get(f'/api/v1/courses/{course.id}/')

    assert response.status_code == 200
    assert response.data['id'] == course.id


@pytest.mark.django_db
def test_get_course_list(client, course_factory):
    """Проверка получения списка курсов"""
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    data = response.data

    assert response.status_code == 200
    assert len(data) == len(courses)


@pytest.mark.django_db
def test_filter_courses_id(client, course_factory):
    """Проверка фильтрации списка курсов по id"""
    courses = course_factory(_quantity=10)
    random_id = choice([course.id for course in courses])
    response = client.get('/api/v1/courses/', data={'id': random_id})
    data = response.json()

    assert response.status_code == 200
    assert data[0]['id'] == random_id


@pytest.mark.django_db
def test_filter_courses_name(client, course_factory):
    """Проверка фильтрации списка курсов по name"""
    courses = course_factory(_quantity=10)
    random_name = choice([course.name for course in courses])
    response = client.get('/api/v1/courses/', data={'name': random_name})
    data = response.json()

    assert response.status_code == 200
    assert data[0]['name'] == random_name


@pytest.mark.django_db
def test_create_course(client):
    """Тест успешного создания курса"""
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'python_course'})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course):
    """Тест успешного обновления курса"""
    get_response = client.get(f'/api/v1/courses/{course.id}/')
    assert get_response.status_code == 200

    put_response = client.put(f'/api/v1/courses/{course.id}/', data={'name': 'New course name'})
    assert put_response.status_code == 200
    assert put_response.data != get_response.data


@pytest.mark.django_db
def test_delete_course(client, course):
    """Тест успешного удаления курса"""
    get_response = client.get(f'/api/v1/courses/{course.id}/')
    assert get_response.status_code == 200

    delete_response = client.delete(f'/api/v1/courses/{course.id}/')
    assert delete_response.status_code == 204

    response_deleted = client.get(f'/api/v1/courses/{course.id}/')
    assert response_deleted.status_code == 404


@pytest.mark.parametrize(
    'students_count,status_code',
    (
        (19, 201),
        (20, 201),
        (21, 400)
    )
)
@pytest.mark.django_db
def test_students_count(settings, students_factory, students_count, status_code, client, course):
    student_count = course.students.count()
    assert settings.MAX_STUDENTS_PER_COURSE >= student_count

    students = students_factory(_quantity=students_count)
    student_ids = [stud.id for stud in students]
    data = {"name": 'New test', "students": student_ids}
    response = client.post('/api/v1/courses/', data=data)
    assert response.status_code == status_code


