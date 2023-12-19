from django.shortcuts import render, get_object_or_404, redirect
from cadastro.models import Usuario 
from cadastro.forms import UsuarioForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "cadastro/partial/principal.html")

def listar(request):
    usuario = Usuario.objects.all()
    return render(request, 'cadastro/partial/listar_usuarios.html', {'usuarios': usuario})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar')
    else:
        form = UsuarioForm()
    return render(request, 'cadastro/partial/formulario_registro.html', {'form': form})

def atualizar_registro(request):
    usuario_id = request.GET.get('pk')
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('/listar')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'cadastro/partial/atualizar_registro.html', {'form': form})

def deletar_registro(request):
     usuario_id = request.GET.get('pk')
     usuario = get_object_or_404(Usuario, pk=usuario_id)
     if request.method == 'POST':
         usuario.delete()
         return redirect('/listar')
     return render(request, 'cadastro/partial/deletar_registro.html', {'usuario': usuario})

def pesquisa_usuario(request):
    nome_p = request.GET.get('nome_pesquisado', '')
    if nome_p != '' :
        usuarios = Usuario.objects.filter(nome__icontains=nome_p)
        return render(request, 'cadastro/partial/pesquisa_usuario.html', {'usuarios': usuarios})
    else:
        return redirect('/listar')

def pesquisa_cpf(request):
    cpf_p = request.GET.get('CPF_pesquisado', '')
    if cpf_p != '' :
        usuarios = Usuario.objects.filter(cpf__icontains=cpf_p)
        return render(request, 'cadastro/partial/pesquisa_cpf.html', {'usuarios': usuarios})
    else:
        return redirect('/listar')
