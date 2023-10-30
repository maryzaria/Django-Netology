from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate_students(self, data):
        if len(data) > settings.MAX_STUDENTS_PER_COURSE:
            raise ValidationError('Превышено количество студентов, макс = 20')
        return data
