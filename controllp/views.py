from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Eat Ass</h1>")

def controll_view(*args, **kwargs):
    return HttpResponse("<h1>minecraft</h1>")