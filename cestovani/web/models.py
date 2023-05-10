from django.db import models
from datetime import datetime

# Create your models here.


class Airports(models.Model):
    city = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.city}({self.code})'


class Flights(models.Model):
    code = models.CharField(max_length=5, default="00000", primary_key=True)
    departure = models.ForeignKey(
        Airports, on_delete=models.CASCADE, related_name='departure')
    departure_date = models.DateTimeField(default=datetime.now, blank=True)
    arrival = models.ForeignKey(
        Airports, on_delete=models.CASCADE, related_name='arrival')
    arrival_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.departure} {self.departure_date.strftime("%d.%m.%y %H:%M")} >> {self.arrival} {self.arrival_date.strftime("%d.%m.%y %H:%M")} (flight no. {self.code})'


class Passangers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    flights = models.ManyToManyField(
        Flights, blank=True, related_name='passanger')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
