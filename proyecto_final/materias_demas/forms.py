from django import forms
from django.contrib import messages
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelChoiceField
from decimal import *
from .models import *
from django.utils.translation import gettext, gettext_lazy as _
