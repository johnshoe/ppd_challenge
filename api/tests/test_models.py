from django.test import TestCase
from ..models import House


class HouseTest(TestCase):

    def setUp(self):
        House.objects.create(
            id=1, transaction_identifier='{BC8936BC-0425-0E2C-E053-6C04A8C0DBF4}')

    def test_house_identifier(self):
        house = House.objects.get(id=1)
        self.assertEqual(house.get_transaction_identifier(),
                         "{BC8936BC-0425-0E2C-E053-6C04A8C0DBF4}")
