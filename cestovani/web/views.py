from django.shortcuts import render
from .models import Flights, Airports

# Create your views here.


def index(request):
    return render(request, 'web/index.html')
