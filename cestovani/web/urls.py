from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:flight_code>', views.flight, name='flight'),
]
