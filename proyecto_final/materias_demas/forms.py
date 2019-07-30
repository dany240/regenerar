from django import forms
from django.contrib import messages
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelChoiceField
from decimal import *
from .models import *
from django.utils.translation import gettext, gettext_lazy as _

class formas_entrada_grados(forms.ModelForm):
    class meta():
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
    class meta():
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
    class meta():
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
            'id_periodo'  :forms.NumberInput(attrs={'class':'form-coontrol'}),
            'fecha_inicio':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
