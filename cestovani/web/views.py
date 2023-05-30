from django.shortcuts import render
from .models import Flights, Airports, Passangers
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def index(request):
    return render(request, 'web/index.html', {
        'flights': Flights.objects.all(),
        'airports': Airports.objects.all()
    })


def flight(request, flight_code):
    flight = Flights.objects.get(pk=flight_code)
    return render(request, 'web/flight.html', {
        'flight': flight,
        'passanger': flight.passanger.all(),
        'none_passanger': Passangers.objects.exclude(flights=flight).all()
    })
