from django.urls import path, re_path
from .views import (
    HouseListView,
    HouseAddView,
    HouseByIdView,
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('houses/', HouseListView.as_view()),
    path('houses/<int:pk>/', HouseByIdView.as_view()),
    path('houses/add', HouseAddView.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)
