from django.shortcuts import render
from .models import usuario


def home(request):
    return render(request, 'usuarios/home.html')
def usuarios (request):
    novo_usuario = usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #exibir todos os usuarios em uma nova pag

    usuarios = {
        'usuarios': usuario.objects.all()
    }
    #retornar os dados para pagina de listagem de usu 
    return render(request, 'usuarios/usuarios.html', usuarios)
