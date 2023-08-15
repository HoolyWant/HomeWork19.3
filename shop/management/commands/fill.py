from django.core.management import BaseCommand

from shop.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        product_list = [
            {'product_name': 'Шото', 'description': 'Ну вот такое оно да',
             'category_name': 'Не знаю даже', 'buy_cost': '10000'},
            {'product_name': 'Ктото', 'description': 'Мы ему не доверяем',
             'category_name': 'Чужой', 'buy_cost': '43545'},
            {'product_name': 'Непонятное', 'description': 'Не понимаем такое',
             'category_name': 'Без комментариев', 'buy_cost': '5009'},
            {'product_name': 'Какоето', 'description': 'СТранное оно',
             'category_name': 'Интересное', 'buy_cost': '399'},
            {'product_name': 'Незнамашо', 'description': 'Ну тут не прибавить не отбавить',
             'category_name': 'Шото', 'buy_cost': '10'},
            {'product_name': 'Невиданное', 'description': 'Не видали раньше',
             'category_name': '???', 'buy_cost': '1234000'},
        ]

        list_for_push = []
        for product in product_list:
            list_for_push.append(
                Product(**product))

        Product.objects.bulk_create(list_for_push)
