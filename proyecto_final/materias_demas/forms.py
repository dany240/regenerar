from django import forms
from django.contrib import messages
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelChoiceField
from decimal import *
from .models import *
from django.utils.translation import gettext, gettext_lazy as _

class formas_entrada_grados(forms.ModelForm):
    class Meta:
        elecciones=(('Mañana','Mañana'),('Tarde','Tarde'))
        model = grado
        fields = [
            'nombre',
            'jornada',
            'salon'
        ]
        labels = {
            'nombre': 'Nombre del grado',
            'jornada': 'Tipo de jornada',
            'salon': 'Numero de salon'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'jornada': forms.Select(attrs={'class': 'form-control'},choices=elecciones),
            'salon': forms.NumberInput(attrs={'class': 'form-coontrol'})
        }


class formas_entrada_materias(forms.ModelForm):
    class Meta:
        model = materia
        fields = [
            'nombre',
            'duracion'
        ]
        labels = {
            'nombre': 'Nombre de la materia',
            'duracion': 'Numero de horas por dia'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'duracion': forms.NumberInput(attrs={'class':'form-coontrol'})
        }


class formas_entrada_periodo(forms.ModelForm):
    class Meta:
        model = periodo
        fields = [
            'id_periodo',
            'fecha_incio',
            'fecha_fin'
        ]
        labels = {
            'id_periodo': 'Identificacion del periodo',
            'fecha_incio': 'Fecha de inicio del periodo',
            'fecha_fin': 'Fecha final del periodo'

        }
        widgets = {
            'id_periodo': forms.NumberInput(attrs={'class': 'form-coontrol'}),
            'fecha_incio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }


class ModelosHeredados(forms.ModelChoiceField):
    labels = ''
    def _init_(self, queryset, to_field_name, labels='', *kwargs):
        self.labels = labels
        super()._init_(queryset=queryset, to_field_name=to_field_name, *kwargs)

    seleccion = ''

    def label_from_instance(self, obj: models.Model):
        var = None
        if self.to_field_name == 'id_grado': var = obj.nombre +': '+obj.jornada
        if self.to_field_name == 'id_materia': var = obj.nombre,
        if self.to_field_name == 'id_periodo': var = obj.fecha_incio + ':'+ obj.fecha_fin,
        if self.to_field_name == 'id_docente':var=obj.id_docente,
        if self.to_field_name== 'id_registro': var= obj.id_material.id_materia +'periodo'+\
                                               obj.id_periodo.fecha_incio+':'+ var.id_periodo.fecha_fin
        if self.to_field_name =='id_estudiante':var= obj.id_persona.nombre +'--'+obj.id_persona.apellido

        return ' {}'.format(var)
class entrada_periodo_materia(forms.ModelForm):
    class Meta:
        fields=[
            'id_material',
            'id_periodo'
        ]
        labels={
            'id_material':'Materia',
            'id_periodo':'periodo'
        }
        widgets={
            'id_materia':ModelosHeredados(queryset=materia.objects.all(),
                                          to_field_name='id_material',
                                          ),
            'id_periodo':ModelosHeredados(queryset=periodo.objects.all()
                                          ,to_field_name='id_periodo',
        )
        }