from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexview (request):
    return HttpResponse("Estas entrando a la vista de productos ")