#-*- coding:utf-8 -*-
from django.forms import ModelForm
from models import Curriculo

class FormCurriculo(ModelForm):
    class Meta:
        model = Curriculo
        exclude = ('foto', )
        
class FormCurriculoFoto(ModelForm):
    class Meta:
        model = Curriculo
        fields = ('foto', )