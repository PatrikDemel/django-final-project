from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.


def users(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
