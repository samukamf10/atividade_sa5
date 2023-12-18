from django.urls import path
from cadastro.views import index, listar, deletar_registro, criar_usuario, atualizar_registro, pesquisa_usuario, pesquisa_cpf

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),
    path('listar/', listar),
    path('deletar_registro/', deletar_registro),
    path('criar_usuario/', criar_usuario),
    path('atualizar_registro/', atualizar_registro),
    path('pesquisa_usuario/', pesquisa_usuario),
    path('pesquisa_cpf/', pesquisa_cpf),
]
