from django.db import models
import sys
sys.path.append(".../proyecto_final")


# Create your models here.

class grado(models.Model):
    id_grado= models.BigAutoField(primary_key=True,db_column='id_grado',null=False,blank=False)
    nombre=models.CharField(db_column='nombre',max_length=10)
    jornada=models.CharField(db_column='jornada',max_length=10)
    salon=models.CharField(db_column='salon',max_length=10)
    class Meta:
        managed = False
        db_table = 'grado'


class  materia(models.Model):
    id_materia=models.BigAutoField(primary_key=True,db_column='id_materia',null=False,blank=False)
    nombre=models.CharField(db_column='nombre',max_length=45)
    duracion=models.IntegerField(db_column='duracion',max_length=3,default=0)
    class Meta:
        managed = False
        db_table = 'materia'


class periodo(models.Model):
    id_periodo=models.BigIntegerField(primary_key=True,db_column='id_periodo',null=False,blank=False)
    fecha_inicio=models.DateField(db_column='fecha_inicio',null=False,blank=False)
    fecha_fin=models.DateField(db_column='fecha_fin',null=False,blank=False)
    class Meta:
        managed = False
        db_table = 'periodo'

