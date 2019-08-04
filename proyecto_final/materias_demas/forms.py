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
                                          ,to_field_name='id_periodo',)
        }

class formas_entrada_persona(forms.ModelForm):
    class Meta:
        model= personas
        fields=[
            'id_personas',
            'nombre',
            'apellido',
            'telefono',
            'fecha_nac',
            'direccion',
            'tipo_doc'
        ]
        labels={
            'id_personas':'Numero de identificacion',
            'nombre':'Nombres',
            'apellido':'Apellidos',
            'celular':'Celular',
            'direccion':'Direccion de Residencia',
            'tipo_doc': 'Tipo de documentos'

        }
        widgets={
            'id_personas':forms.NumberInput(attrs={'class':'form-coontrol'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nac':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_doc': forms.Select(attrs={'class': 'form-control'})

        }
class formas_camabiar_personas(forms.ModelForm):
    class Meta:
        model=personas
        fields=[
            'id_personas',
            'nombre',
            'apellido',
            'telefono',
            'fecha_nac',
            'tipo_doc'
        ]
        labels={
            'nombre':'Nombre ',
            'apellido' :'Apellido',
            'telefono':'telefono',
            'fecha_nac':'Fecha de nacimiento',
            'tipo_doc':'Tipo de documentos'
        }
        widgets = {
            'cedula': forms.NumberInput(attrs={'class': 'form-control', 'min': '999999999'}),
            'nombre_doc': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_doc': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nac': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'celular': forms.NumberInput(attrs={'class': 'form-control', 'min': '99999', 'max': '9999999999'}),
            'tipo_doc':forms.Select(attrs={'class': 'form-control'})

        }
class formas_entradas_docentes(forms.ModelForm):

# clase donde se ponen todos los atributos a modificar
    class Meta:
        model = docentes #modelo a referenciar
        fields = [ # atributos que quiero mostrar
            'grado_carrera',
            'especializacion',
        ]
        labels = { # text que muestra en el html
            'grado_carrera': 'Carrera Universitaria',
            'especializacion':'especializacion',
        }
        widgets = {# que tipo de importaciones vamos a hacer con las variables
            'grado_carrera': forms.TextInput(attrs={'class': 'form-control'}),
            'especializacion': forms.Select(attrs={'class': 'form-control'}),
        }

class validar_contraseñas(forms.Form):
    def __int__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)


    error_messages = {
        'password_mismatch': _("las dos contraseñas no "
                               "coiciden."),
    }
    password1 = forms.CharField(label=_("Contraseña"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                )
    password2 = forms.CharField(label=_("contraseña de confrmacion"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=_("Revise su contraseña"),
                                )
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)

#class registro_user(UserCreationForm):
#    class Meta:
#        model = personas.objects.usuario
#        fields = [
#            'username',
#            'first_name',
#            'lasr_name'
#        ]

 #       labels = {
 #           'username': 'Nombre de usuario',
 #           'first_name': 'Primer nombre',
 #           'lasr_name': 'Segundo nombre'
 #       }