from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Hra


class HraModelForm(ModelForm):
    class Meta:
        model = Hra
        fields = '__all__'