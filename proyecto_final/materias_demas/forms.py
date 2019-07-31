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
        model= grado
        fields = [
            'id_grado',
            'nombre',
            'jornada',
            'salon'
        ]
        labels = {
            'id_grado' : 'Identificacion de grado',
            'nombre': 'Nombre del grado',
            'jornada' : 'Tipo de jornada',
            'salon' : 'Numero de salon'

        }
        widgets = {
            'id_grado' :forms.NumberInput(attrs={'class':'form-coontrol'}),
            'nombre' :forms.TextInput(attrs={'class':'form-control'}),
            'jornada' : forms.Select(attrs={'class': 'form-control'}),
            'salon' :forms.NumberInput(attrs={'class':'form-coontrol'})
        }


class formas_entrada_materias(forms.ModelForm):
    class Meta:
        model=materia
        fields = [
            'id_materia',
            'nombre',
            'duracion'
        ]
        labels = {
            'id_materia' : 'Identificacion de materia',
            'nombre' : 'Nombre de la materia',
            'duracion': 'Numero de horas'
        }
        widgets = {
            'id_materia' :forms.NumberInput(attrs={'class':'form-coontrol'}),
            'nombre' :forms.TextInput(attrs={'class':'form-control'}),
            'duracion':forms.NumberInput(attrs={'class':'form-coontrol'})
        }


class formas_entrada_periodo(forms.ModelForm):
    class Meta:
        model=periodo
        fields = [
            'id_periodo',
            'fecha_incio',
            'fecha_fin'
        ]
        labels = {
            'id_periodo' : 'Identificacion del periodo',
            'fecha_incio' : 'Fecha de inicio del periodo',
            'fecha_fin' : 'Fecha final del periodo'

        }
        widgets = {
            'id_periodo': forms.NumberInput(attrs={'class': 'form-coontrol'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
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
        if self.to_field_name == 'id_periodo': var = obj.id_periodo,
        if self.to_field_name == 'id_docente':var.id_docente
        if self.to_field_name== 'id_registro': var.id_material.id_materia +'periodo'+\
                                               var.id_periodo.fecha_incio+':'+ var.id_periodo.fecha_fin
        return ' {}'.format(var)