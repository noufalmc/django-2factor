from django import forms
from .models import CodesFactor


class CodeFactorForms(forms.ModelForm):
    class Meta:
        model = CodesFactor
        fields =('number',)