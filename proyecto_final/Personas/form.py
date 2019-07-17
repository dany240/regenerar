from django import forms
from django.contrib import messages
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelChoiceField
from decimal import *
from .models import *
from django.utils.translation import gettext, gettext_lazy as _

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
            'celular': forms.NumberInput(attrs={'class': 'form-control', 'min': '99999', 'max': '9999999999'}),
            'tipo_doc':forms.Select(attrs={'class': 'form-control'})

        }
class formas_entradas_docentes(forms.ModelForm):


    class Meta:
        model = docentes
        fields = [
            'grado_carrera',
            'especializacion',
        ]
        labels = {
            'grado_carrera': 'Carrera Universitaria',
            'especializacion':'especializacion',
        }
        widgets = {
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