from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from datetime import date, datetime
from django.utils.dateparse import parse_date

from .serializer import HouseSerializer
from .models import House
from .filters import HouseFilter


# Houses
class HouseListView(generics.ListAPIView):
    serializer_class = HouseSerializer
    filterset_class = HouseFilter
    paginate_by = 20

    def get_queryset(self):
        queryset = House.objects.all()
        return queryset


class HouseByIdView(generics.RetrieveAPIView):
    serializer_class = HouseSerializer

    def get_queryset(self):
        queryset = House.objects.filter(pk=self.kwargs['pk'])
        return queryset


class HouseAddView(generics.CreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
