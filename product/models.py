from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    price = models.FloatField()

    def __str__(self):
        return self.name