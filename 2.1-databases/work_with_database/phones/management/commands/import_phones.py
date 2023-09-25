import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            ph = {
                **phone,
                'slug': slugify(phone.get('name', 'phone'))
            }
            Phone.objects.update_or_create(id=ph.get('id'), defaults=ph
                # id=int(phone.get('id')),
                # name=phone.get('name', 'phone'),
                # price=int(phone.get('price', 0)),
                # image=phone.get('image'),
                # release_date=phone.get('release_date'),
                # lte_exists=phone.get('lte_exists'),
                # slug=slugify(phone.get('name', 'phone'))
            )
