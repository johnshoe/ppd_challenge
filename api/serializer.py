from rest_framework import serializers
from .models import House


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('transaction_identifier', 'price', 'date_of_transfer', 'postal_code',
                  'property_type', 'old_new', 'duration', 'paon', 'saon', 'street',
                  'locality', 'town', 'district', 'country', 'ppd_cat', 'record_stat')
