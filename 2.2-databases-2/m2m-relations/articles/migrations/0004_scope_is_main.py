# Generated by Django 4.2.5 on 2023-10-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_scope_options_alter_tag_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=True, verbose_name='Основной'),
        ),
    ]
