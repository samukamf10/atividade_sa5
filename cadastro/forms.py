from django import forms
from .models import Usuario 

class UsuarioForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput())
    cpf = forms.CharField(widget=forms.TextInput(attrs={'data-mask':"000.000.000-00", 'minlength': 14}))
    email = forms.EmailField(widget=forms.EmailInput())
    telefone = forms.CharField(widget=forms.TextInput(attrs={'data-mask':"(00) 99999-9999", 'maxlength': 14}))
    class Meta:
       model = Usuario 
       fields = ['nome', 'cpf', 'email', 'telefone']
