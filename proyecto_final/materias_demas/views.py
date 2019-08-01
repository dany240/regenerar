from typing import Dict, Any

from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.http.request import *
from .models import *
from django.db import models
from .forms import *
from django.http.response import *
from .models import  *

# Create your views here.

def materias(request):
    formas = None
    if (request.method == 'POST'):
        formas = formas_entrada_materias(request.POST)
        if (formas.is_valid()):
            formas.save()
            return HttpResponse('<h1> Materias guardadas </h1>')

    else:
        formas = formas_entrada_materias
        return render(request, template_name='html/Create/'
                                             'contenido.html',
                      context={
                          'formas': formas
                      })

def grados(request):
    formas = formas_entrada_grados
    if (request.method == 'POST'):
        formas = formas_entrada_grados(request.POST)
        if (formas.is_valid()):
            formas.save()
            return HttpResponse('<h1> Grados guardados </h1>')

    else:
        formas = formas_entrada_grados
        return render(request, template_name='html/Create/'
                                             'contenido.html',
                      context={
                          'formas': formas
                      })

def cargar_periodo (request):
    formas = None
    if (request.method == 'POST'):
        formas = formas_entrada_periodo(request.POST)
        if (formas.is_valid()):
            formas.save()
            return HttpResponse('<h1> Periodos Guardados </h1>')

    else:
        formas = formas_entrada_periodo
        return render(request, template_name='html/Create/'
                                             'contenido.html',
                      context={
                          'formas': formas
                      })
def periodo_actualizar(request:HttpRequest,id_periodo):
    periodo_ant= periodo.objects.get(id_periodo=id_periodo)
    forma=formas_entrada_periodo(instance=periodo_ant)#passando informacion al form
    if(request.method =='POST'):
        forma=formas_entrada_periodo(request.POST,instance=periodo_ant)
        if(forma.is_valid()):
            forma.save()
            return HttpResponse('<h1> Periodo Actualizado </h1>')
        else:
            messages.add_message(request)
    else:
        return render(request,
                      template_name='html/Create/'
                                    'contenido.html',
                      context={
                          'formas': forma
                      })

def grado_actualizar(request:HttpRequest, id_grado):
    grado_ant = grado.objects.get(id_grado=id_grado)
    forma = formas_entrada_grados(instance=grado_ant)
    if (request.method == 'POST'):
        forma=formas_entrada_grados(request.POST, instance=grado_ant)
        if(forma.is_valid()):
            forma.save()
            return redirect( 'list_grad')
        else:
            messages.add_message(request)
    else:
        return render(request,
                      template_name='html/Create/'
                                    'contenido.html',
                      context={
                          'formas': forma
                      })

def materia_actualizar(request:HttpRequest, id_materia):
    materia_ant = materia.objects.get(id_materia=id_materia)
    forma = formas_entrada_materias(instance=materia_ant)
    if (request.method == 'POST'):
        forma=formas_entrada_materias(request.POST, instance=materia_ant)
        if(forma.is_valid()):
            forma.save()
            return HttpResponse('<h1> Materia actualizada <h1>')
        else:
            messages.add_message(request)
    else:
        return render(request,
                      template_name='html/Create/'
                                    'contenido.html',
                      context={
                          'formas': forma
                      })

def grado_estudiantes_insertar(request):
    pass

def listar_periodo(request):
    period = periodo.objects.all()
    return render(request, template_name='html/Listar_m/Listar_periodo.html', context={'forma': period})

def listar_grado(request):
    grad = grado.objects.all()
    return render(request, template_name='html/Listar_m/listar_grado.html', context={'forma': grad})

def listar_materia(request):
    mater = materia.objects.all()
    return render(request, template_name='html/Listar_m/listar_materia.html', context={'forma': mater})