from django.contrib.gis.db.models import PolygonField
from django.db import models
from djmoney.models.fields import MoneyField


class StrMixin:
    def __str__(self):
        return self.name


class Company(StrMixin, models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=256)

    def __str__(self):
        return "{} ({})".format(self.name, self.address)


class ServiceArea(StrMixin, models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    poly = PolygonField()


class ServiceType(StrMixin, models.Model):
    name = models.CharField(max_length=256, unique=True)


class ServiceTypeAreaPrice(models.Model):
    area = models.ForeignKey(ServiceArea, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='RUB')

    def __str__(self):
        return '{} за {} в {}'.format(self.price, self.service_type, self.area)
