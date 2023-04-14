import datetime

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    event = models.CharField(max_length=50, blank=False, null=False, default='Birthday')
    age = models.IntegerField()
    caketype = models.CharField(max_length=50, blank=False, null=False)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    phone = models.IntegerField()
    # gender = models.CharField(max_length=50, blank=False, null=False)
    orderdate = models.DateField()
    deliverydate = models.DateField()


def __str__(self):
    return self.name


