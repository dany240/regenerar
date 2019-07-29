from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http.request import *
from .models import *
from django.db import models
from .forms import *
from django.http.response import *
# Create your views here.

def materias(request):
    return HttpResponse("insert_materia")

def grados(request):
    return HttpResponse("insert_grado")

def periodo (request):
    return HttpResponse("insert_periodo")