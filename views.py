from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Customer
# Create your views here.
def slatt(request):
    return  HttpResponse(200)