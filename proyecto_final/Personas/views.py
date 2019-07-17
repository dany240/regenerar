from django.shortcuts import render
from django.http.request import *
from .models import *
from django.db import models
from .form import *
from django.http.response import *
# Create your views here.
"""clases de prueba"""
def retornar(request:HttpRequest):
    return HttpResponse('<h1>largo</h1>')
def prueba_html(request:HttpRequest):
    return render(request,'html/pruebas.html')
# ___________________________________________________

"""metodos para personas"""
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
                                             'personas.html',
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
            return HttpResponse('<h1> personas guardas </h1>')

        return HttpResponse('<h1> personas no  </h1>')
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