from product.models import Product
from product.views import ProductDetail
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Get product details byProduct Id'

    def add_arguments(self, parser):
        parser.add_argument('product_id', nargs='+',type=int)

    def handle(self, *args, **options):

            for pk in options['product_id']:
                products= Product.objects.get(id=pk)
                self.stdout.write(self.style.SUCCESS('id: "%d",' % products.id))
                self.stdout.write(self.style.SUCCESS('name: "%s",'% products.name))
                self.stdout.write(self.style.SUCCESS('type: "%s",' % products.type))
                self.stdout.write(self.style.SUCCESS('price: "%f",' % products.price))
