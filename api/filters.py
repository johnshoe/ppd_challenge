from django_filters import rest_framework as filters
from .models import House


class HouseFilter(filters.FilterSet):

    class Meta:
        model = House
        fields = {
            'transaction_identifier': ['iexact']
        }
