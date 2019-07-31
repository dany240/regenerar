from django.conf.urls import  url
from django.urls import include, path

from .views import *
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt


urlpatterns=[
    url(r'^listar_persona$',listar_persona,name='listar_persona'),
    url(r'^pruebas',prueba_html,name='pruebas'),
    url(r'^retornar$',retornar,name='retornar'),
    url(r'^crear_personas$',crear_personas,name='crear_personas'),
    url(r'^crear_docentes$',crear_docente,name='crear_docentes')
]
