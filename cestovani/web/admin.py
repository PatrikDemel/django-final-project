from django.contrib import admin
from .models import Airports, Flights, Passangers

# Register your models here.
admin.site.register(Airports)
admin.site.register(Flights)
admin.site.register(Passangers)
