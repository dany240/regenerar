from django.db import models
from django.contrib.auth.models import *
# Create your models here.


class personas(models.Model):
    tipo_documentos=(
        ('CC','Cedula')
        ,('TI','Tarjeta identidad')
        ,('OT','Otros')

    )
    id_personas=models.BigIntegerField(primary_key=True,db_column='id_personas',null=False,blank=False)
    nombre=models.TextField(db_column='nombre',blank=False,null=False)
    apellido=models.TextField(db_column='apellido',blank=False,null=False)
    direccion=models.TextField(db_column='direccion',blank=False)
    telefono=models.CharField(db_column='telefono',max_length=10)
    fecha_nac=models.DateField(db_column='fecha_nac',blank=False,null=False,max_length=10)
    tipo_doc=models.CharField(choices=tipo_documentos,db_column='tipo_doc',blank=False,null=False,max_length=7)
    usuario=models.OneToOneField(User,on_delete=models.PROTECT,db_column='users')
    class Meta:
        managed = False
        db_table = 'personas'

class estudiantes (models.Model):
    id_estudiante=models.BigAutoField(primary_key=True,db_column='id_estudiante',null=False,blank=False)
    id_persona=models.ForeignKey(personas,related_name='persona_est',on_delete=models.PROTECT,db_column='id_persona')
    grado_esc=models.IntegerField(db_column='grado_esc',max_length=3,null=False,blank=False)
    class Meta:
        managed = False
        db_table = 'estudiante'
class docentes(models.Model):
    selecion = (
         ('Normalista','Normalista')
        ,('licenciado', 'licenciado')
        ,('especializacion', 'especializacion')
        ,('Maestria', 'Maestria')
        ,('Doctorado','Doctorado')
        ,('otros','otros')
    )
    id_docentes=models.BigAutoField(primary_key=True,db_column='id_docente',null=False,blank=False)
    id_persona=models.ForeignKey(personas,related_name='persona_doc',on_delete=models.PROTECT,db_column='id_persona')
    especializacion= models.CharField(choices=selecion,
    db_column='especializacion',max_length=100)
    grado_carrera= models.CharField(db_column='grado_carrera',max_length=100)


    class Meta:
        managed = False
        db_table = 'docentes'
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
    fecha_incio=models.DateField(db_column='fecha_incio',null=False,blank=False)
    fecha_fin=models.DateField(db_column='fecha_fin',null=False,blank=False)
    class Meta:
        managed = False
        db_table = 'periodo'


class materia_periodo(models.Model):
    id_registro=models.BigAutoField(primary_key=True,null=False,blank=False,db_column='id_registro')
    id_material=models.ForeignKey(materia,related_name='materia_per1',on_delete=models.PROTECT,db_column='id_materia')
    id_periodo=models.ForeignKey(periodo,related_name='materia_per2',on_delete=models.PROTECT,db_column='id_periodo')
    class Meta:
        managed = False
        db_table = 'materia_periodo'
        unique_together=('id_periodo','id_material')

class doc_mater_per(models.Model):
    id_registro=models.ForeignKey(materia_periodo,related_name='materia_per_doc1',on_delete=models.PROTECT,db_column='id_registro')
    id_grado=models.ForeignKey(grado,related_name='materia_per_doc2',on_delete=models.PROTECT,db_column='id_grado')
    id_docente=models.ForeignKey(docentes,related_name='materia_per_doc3',on_delete=models.PROTECT,db_column='id_docente')
    class Meta:
        managed = False
        db_table = 'doc_mater_per'
        unique_together=('id_registro','id_grado','id_docente')
class notas(models.Model):
    id_estudiante=models.ForeignKey(estudiantes,related_name='notas2',on_delete=models.PROTECT,db_column='id_estudiante')
    id_registro=models.ForeignKey(materia_periodo,related_name='notas1',on_delete=models.PROTECT,db_column='id_registro')
    notas=models.DecimalField(decimal_places=2,max_digits=3,default=0)
    class Meta:
        managed = False
        db_table = 'notas'
        unique_together=('id_estudiante','id_registro')

class grado_estudiantes(models.Model):
    id_estudiante=models.ForeignKey(estudiantes,related_name='grado_estudiantes',on_delete=models.PROTECT,db_column='id_estudiante')
    id_grado=models.ForeignKey(grado,related_name='grado_estudiantes1',on_delete=models.PROTECT,db_column='id_grado')
    fec_ini=models.DateField(db_column='fec_ini',blank=False,null=False)
    fec_fin=models.DateField(db_column='fec_fin',blank=False,null=False)

    class Meta:
        managed = False
        db_table = 'grado_estudiantes'
        unique_together=('id_estudiante','id_grado','fec_ini','fec_fin')







