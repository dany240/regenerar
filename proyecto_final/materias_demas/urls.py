from django.conf.urls import  url
from django.urls import include, path

from .views import *
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    #url(),
    url(r'^cargar_materia',materias,name='materia'), #como se realza una url
    url(r'^cargar_grado',grados,name='grado'),
    url(r'^cargar_periodo',cargar_periodo,name='periodo'),
    url(r'^listar_periodo',listar_periodo, name='list_period'),
    url(r'^listar_grado',listar_grado, name='list_grad'),
    url(r'^listar_materia',listar_materia, name='list_mater'),
    url(r'^actualizar_periodo/(?P<id_periodo>\d+)$',periodo_actualizar, name ='actual_period'),
    url(r'^actualizar_grado/(?P<id_grado>\d+)$',grado_actualizar, name ='actual_grad'),
    url(r'^actualizar_materia/(?P<id_materia>\d+)$',materia_actualizar, name ='actual_mater'),
]