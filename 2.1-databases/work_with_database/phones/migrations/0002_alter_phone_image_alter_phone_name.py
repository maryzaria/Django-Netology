# Generated by Django 4.2.5 on 2023-09-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
