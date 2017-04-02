from product.models import Product
from product.views import ProductDetail
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Get All Products'

    def handle(self, *args, **options):
        products = Product.objects.all()
        for prodct in products:
            self.stdout.write(self.style.SUCCESS('id: "%d",' % prodct.id))
            self.stdout.write(self.style.SUCCESS('name: "%s",' % prodct.name))
            self.stdout.write(self.style.SUCCESS('type: "%s",' % prodct.type))
            self.stdout.write(self.style.SUCCESS('price: "%f",' % prodct.price))