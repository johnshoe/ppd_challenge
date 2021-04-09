from django.db import models


class House(models.Model):
    transaction_identifier = models.CharField(
        max_length=80, default="", unique=True)
    price = models.CharField(max_length=12, null=True,)
    date_of_transfer = models.DateTimeField(null=True,)
    postal_code = models.CharField(max_length=12, null=True,)
    property_type = models.CharField(max_length=2, null=True,)
    old_new = models.CharField(max_length=2, null=True,)
    duration = models.CharField(max_length=2, null=True,)
    paon = models.CharField(max_length=100, null=True,)
    saon = models.CharField(max_length=100, null=True,)
    street = models.CharField(max_length=100, null=True,)
    locality = models.CharField(max_length=100, null=True,)
    town = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True,)
    country = models.CharField(max_length=100, null=True,)
    ppd_cat = models.CharField(max_length=100, null=True,)
    record_stat = models.CharField(max_length=100, null=True,)
    currency = models.CharField(max_length=4, null=True,)

    def __str__(self):
        return self.name

    def get_transaction_identifier(self):
        return self.transaction_identifier
