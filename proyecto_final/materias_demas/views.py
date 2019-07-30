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
    formas = None
    if (request.method == 'POST'):
        formas = formas_entrada_materias(request.POST)
        if (formas.is_valid()):
            formas.save()
            return HttpResponse('<h1> personas guardas </h1>')

    else:
        formas = formas_entrada_materias
        return render(request, template_name='html/Create/'
                                             'personas.html',
                      context={
                          'formas': formas
                      })

def grados(request):
    formas = None
    if (request.method == 'POST'):
        formas = formas_entrada_grados(request.POST)
        if (formas.is_valid()):
            formas.save()
            return HttpResponse('<h1> Grados guardados </h1>')

    else:
        formas = formas_entrada_grados
        return render(request, template_name='html/Create/'
                                             'grados.html',
                      context={
                          'formas': formas
                      })

def periodo (request):
    formas = None
    if (request.method == 'POST'):
        formas = formas_entrada_periodo(request.POST)
        if (formas.is_valid()):
            formas.save()
            return HttpResponse('<h1> personas guardas </h1>')

    else:
        formas = formas_entrada_periodo
        return render(request, template_name='html/Create/'
                                             'personas.html',
                      context={
                          'formas': formas
                      })