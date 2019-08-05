from typing import Dict, Any

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from django.shortcuts import render
from django.http.request import *
from .models import *
from django.db import models
from .forms import *
from django.http.response import *
from .models import  *

# Create your views here.


def retornar(request:HttpRequest):
    return HttpResponse('<h1>Bienevenido a algo que no sirve</h1>')
def prueba_html(request:HttpRequest):
    return render(request,'html/pruebas.html')

def cargar_materias(request):
    formas = None
    if (request.method == 'POST'):
        formas = formas_entrada_materias(request.POST)
        if (formas.is_valid()):
            formas.save()
            return redirect('list_mater')
    else:
        formas = formas_entrada_materias
        return render(request, template_name='html/Create/'
                                             'contenido.html',
                      context={
                          'formas': formas
                      })


def cargar_grados(request):
    formas = formas_entrada_grados
    if (request.method == 'POST'):
        formas = formas_entrada_grados(request.POST)
        if (formas.is_valid()):
            formas.save()
            return redirect('list_grad')
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
            return redirect('list_period')
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
            return redirect('list_period')
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
            return redirect('list_grad')
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
            return redirect('list_mater')
        else:
            messages.add_message(request)
    else:
        return render(request,
                      template_name='html/Create/'
                                    'contenido.html',
                      context={
                          'formas': forma
                      })


def eliminar_periodo(request:HttpRequest, id_periodo):
    period = periodo.objects.get(id_periodo=id_periodo)
    if (request.method == 'POST'):
        period.delete()
        return redirect('list_period')
    else:
        return render(request,
                      template_name='html/delete_m/'
                                    'delete_m.html',
                      context={'forma': period}
                      )


def eliminar_materia(request:HttpRequest, id_materia):
    mater = materia.objects.get(id_materia=id_materia)
    if (request.method == 'POST'):
        mater.delete()
        return redirect('list_mater')
    else:
        return render(request,
                      template_name='html/delete_m/'
                                    'delete_m.html',
                      context = {'forma': mater}
                      )


def eliminar_grado(request:HttpRequest, id_grado):
    grad = grado.objects.get(id_grado=id_grado)
    if (request.method == 'POST'):
        grad.delete()
        return redirect('list_grad')
    else:
        return render(request,
                      template_name='html/delete_m/'
                                    'delete_m.html',
                      context={'forma': grad}
                      )


def listar_periodo(request):
    period = periodo.objects.all()
    return render(request, template_name='html/Listar_m/Listar_periodo.html', context={'forma': period})


def listar_grado(request):
    grad = grado.objects.all()
    return render(request, template_name='html/Listar_m/listar_grado.html', context={'forma': grad})


def listar_materia(request):
    mater = materia.objects.all()
    return render(request, template_name='html/Listar_m/listar_materia.html', context={'forma': mater})

#def registrar_usuario (request):
#    form = None
#    if (request.method == 'POST'):
#        form = registro_user
#        if form.is_valid():
#            form.save()
#            redirect('list_period')
#    else:
#        form = registro_user
#        return render(request, template_name='html/Create/contenido.html', context={'forma': form})


def login (request:HttpRequest):
    if (request.method == 'POST'):
        redirect('list_grad')
    else:
        return render(request, template_name='html/Create/login.html')
    #username = request.POST['username']
    #pasword = request.POST['password']
    #user = authenticate(request, username=username, password=pasword)
    #if user is not None:
    #    login(request, user)
    #    return redirect('list_grad')
    #else:
    #    return render(request, template_name='html/Create/login.html', context={'forma': user})


def periodo_materia_insertar(request):
    pass


def crear_personas(request:HttpRequest):
    formas=None
    if(request.method=='POST'):
        formas=formas_entrada_persona(request.POST)
        if(formas.is_valid()):
            formas.save()
            return HttpResponse('<h1> personas guardas </h1>')
    else:
        formas=formas_entrada_persona
        return  render(request,template_name='html/Create/'
                                             'contenido.html',
                       context={
            'formas':formas
        })

def listar_persona(request:HttpRequest):
    var=personas.objects.all()
    return HttpResponse ('<h1>datos {}'.format(var))
"""metodos para docentes"""

def c_dict(request,filds:forms.ModelForm):
    recorrer=filds.Meta.fields
    diccinario={}
    for x in recorrer:
        diccinario[x]=request.POST[x]
    return  diccinario

def crear_docente(request:HttpRequest):
    personas_n=formas_entrada_persona
    formas=formas_entradas_docentes
    usuarios=validar_contraseñas
    if(request.method=='POST'):
        formas=formas_entradas_docentes(c_dict(request,formas_entradas_docentes))
        personas_n=formas_entrada_persona(c_dict(request,formas_entrada_persona))
        if( personas_n.is_valid() and formas.is_valid() ):
            usuarios = validar_contraseñas(c_dict(request, validar_contraseñas))
            persona_final=personas_n.save(commit=False)#type:personas
            us=usuarios.save(commit=False) #type:User
            docente=formas.save(commit=False)#type:docentes
            us.username=request.POST['id_personas']
            us.save()
            persona_final.usuario=us
            persona_final.save()
            docente.id_persona=persona_final
            docentes.save()
            return HttpResponse('<h1> Docentes guardas </h1>')
        else :
            return HttpResponse('<h1> Docentes no  guardadas</h1>')
    else:
        formas=formas_entradas_docentes
        personas_n=formas_entrada_persona
        return  render(request,template_name='html/Create/'
                                             'docentes.html',
                       context={
            'formas':formas,
            'pesonas':personas_n,
            'usuarios':usuarios
        })