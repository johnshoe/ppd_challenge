from django_filters import rest_framework as filters
from .models import House


class HouseFilter(filters.FilterSet):
    start = filters.IsoDateTimeFilter(
        field_name="date_of_transfer", lookup_expr='gte')
    end = filters.IsoDateTimeFilter(
        field_name="date_of_transfer", lookup_expr='lte')

    class Meta:
        model = House
        fields = {
            'transaction_identifier': ['iexact'],
        }
