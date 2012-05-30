from django import forms

from .models import Fornecedor, Cliente


class UploadFileForm(forms.Form):
    file = forms.FileField()


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
