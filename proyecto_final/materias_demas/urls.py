from django.conf.urls import  url
from django.urls import include, path

from .views import *
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    #url(),
    url(r'^loguear',login,name='login'),
#    url(r'^registrar',registrar_usuario,name='registre'),
    url(r'^pruebas',prueba_html,name='pruebas'),
    url(r'^retornar$',retornar,name='retornar'),
    url(r'^listar_persona$',listar_persona,name='listar_persona'),
    url(r'^crear_personas$',crear_personas,name='crear_personas'),
    url(r'^crear_docentes$',crear_docente,name='crear_docentes'),
    url(r'^cargar_materia',cargar_materias,name='materia'), #como se realza una url
    url(r'^cargar_grado',cargar_grados,name='grado'),
    url(r'^cargar_periodo',cargar_periodo,name='periodo'),
    url(r'^cargar_lectivo', cargar_lectivo, name='lectivo'),
    url(r'^cargar_period_mater', cargar_periodo_materia, name='periodo_materia'),
    url(r'^listar_periodo',listar_periodo, name='list_period'),
    url(r'^listar_grado',listar_grado, name='list_grad'),
    url(r'^listar_materia',listar_materia, name='list_mater'),
    url(r'^listar_lectivo',listar_lectivo, name='list_lectiv'),
    url(r'^listar_period_mater',listar_periodo_materia, name='list_period_mater'),
    url(r'^actualizar_periodo/(?P<id_periodo>\d+)$',periodo_actualizar, name ='actual_period'),
    url(r'^actualizar_lectivo/(?P<id>\d+)$', lectivo_actualizar, name='actual_lectiv'),
    url(r'^actualizar_grado/(?P<id_grado>\d+)$',grado_actualizar, name ='actual_grad'),
    url(r'^actualizar_materia/(?P<id_materia>\d+)$',materia_actualizar, name ='actual_mater'),
    url(r'^actualizar_period_mater/(?P<id_registro>\d+)$',periodo_materia_actualizar, name ='actual_period_mater'),
    url(r'^eliminar_periodo/(?P<id_periodo>\d+)$',eliminar_periodo, name ='eliminar_period'),
    url(r'^eliminar_lectivo/(?P<id>\d+)$',eliminar_lectivo, name ='eliminar_lectiv'),
    url(r'^eliminar_materia/(?P<id_materia>\d+)$',eliminar_materia, name ='eliminar_mater'),
    url(r'^eliminar_grado/(?P<id_grado>\d+)$',eliminar_grado, name ='eliminar_grad'),
    url(r'^eliminar_period_mater/(?P<id_registro>\d+)$',eliminar_periodo_materia, name ='eliminar_period_mater')
]