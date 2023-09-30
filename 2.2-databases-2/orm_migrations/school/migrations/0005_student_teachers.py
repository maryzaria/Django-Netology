# Generated by Django 4.2.5 on 2023-09-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_remove_student_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='school.teacher'),
        ),
    ]
