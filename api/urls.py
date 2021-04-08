from django.urls import path
from .views import HouseListView, HouseAddView, HouseByIdView, HouseByDateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('houses/', HouseListView.as_view()),
    path('houses/<int:pk>/', HouseByIdView.as_view()),
    path('houses/add', HouseAddView.as_view()),
    path('houses/<str:pk>/', HouseByDateView.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)
