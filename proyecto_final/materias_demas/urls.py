from django.conf.urls import  url
from django.urls import include, path

from .views import *
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    url(r'^Listar_materia',materias,name='materia'), #como se realza una url
    url(r'^Listar_grado',grados,name='grado'),
    url(r'^Listar_periodo',periodo,name='periodo'),
]