#-*- coding: utf-8 -*-
from django import forms
from django.db.models import Q
from django.forms import ModelForm
from models import Foto, Galeria, UploadArquivo
from micro.middleware import threadlocals
from django.contrib.admin import widgets

class FormGaleria(ModelForm):   
    fotos = forms.ModelMultipleChoiceField(Foto.objects.all())
    
    class Meta:
        model = Galeria

    def __init__(self, *args, **kwargs):
        super(FormGaleria, self).__init__(*args, **kwargs)
        if threadlocals.get_current_user().is_superuser:
            self.fields['fotos'] = forms.ModelMultipleChoiceField(Foto.objects.all(), 
                widget = widgets.FilteredSelectMultiple(verbose_name = "Fotos", is_stacked = False), required = False)
            self.fields['arquivo'] = forms.ModelMultipleChoiceField(UploadArquivo.objects.all(), 
                widget = widgets.FilteredSelectMultiple(verbose_name = "Arquivos", is_stacked = False), required = False, label="Arquivos")
        else:
            self.fields['fotos'] = forms.ModelMultipleChoiceField(Foto.objects.filter(Q(autor = threadlocals.get_current_user()) | Q(publico = True)), 
                widget = widgets.FilteredSelectMultiple(verbose_name = "Fotos", is_stacked = False), required = False)
            self.fields['arquivo'] = forms.ModelMultipleChoiceField(UploadArquivo.objects.filter(Q(autor = threadlocals.get_current_user()) | Q(publico = True)), 
                widget = widgets.FilteredSelectMultiple(verbose_name = "Arquivos", is_stacked = False), required = False, label = "Arquivos")
        
class FormAdminArquivo(ModelForm):
    class Meta:
        model = UploadArquivo
    
    def clean_arquivo(self):
        arquivo = self.cleaned_data['arquivo']
        arquivo_nome = self.cleaned_data['arquivo'].name
        if not arquivo_nome.endswith(".zip"):
            raise forms.ValidationError(u'O arquivo selecionado n\u00E3o possui a extens\u00E3o .zip')
        if not arquivo._size < 10485760:
            raise forms.ValidationError(u'O arquivo selecionado tem que ter menos de 2.5 MB de tamanho.')
        return self.cleaned_data['arquivo']