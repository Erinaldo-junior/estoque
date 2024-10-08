from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from .models import Estoque

def login(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect('home')
        else:
            return HttpResponse('Email ou senha inválidos')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        username = request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        first_name = request.POST.get('nome')

        if User.objects.filter(username=username).exists():
            return HttpResponse('Usuário já existe!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
            user.save()
            return redirect('login')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/home.html')
    else:
        return redirect('login')

def lancar(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == "POST":
        item = Estoque()
        item.nome = request.POST.get('nome')
        item.item = request.POST.get('item')
        try:
            item.quantidade = int(request.POST.get('quantidade'))
        except ValueError:
            return HttpResponse("A quantidade deve ser um número válido.")
        
        if not item.nome or not item.item or item.quantidade is None:
            return HttpResponse("Todos os campos são obrigatórios.")
        
        if Estoque.objects.filter(nome=item.nome, item=item.item).exists():
            return HttpResponse("Este item já foi cadastrado.")
        
        item.user = request.user  # Atribuindo o usuário autenticado
        try:
            item.save()
            return redirect('home')
        except Exception as e:
            return HttpResponse(f"Erro ao salvar o item: {str(e)}")
    else:
        return render(request, 'usuarios/lancar.html')

def visualizar(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == "GET":
        lista_Item = Estoque.objects.all()
        lista_opcoes = Estoque.objects.values_list('item', flat=True).distinct()
        dicionarios = {
            "lista_Item": lista_Item,
            "lista_opcoes": lista_opcoes
        }
        return render(request, 'usuarios/visualizar.html', dicionarios)
    else:
        categoria = request.POST.get('categoria')
        if categoria == "Todas as categorias":
            lista_Item = Estoque.objects.all()
        else:
            lista_Item = Estoque.objects.filter(item=categoria)
        
        lista_opcoes = Estoque.objects.values_list('item', flat=True).distinct()
        dicionarios = {
            "lista_Item": lista_Item,
            "lista_opcoes": lista_opcoes
        }
        return render(request, 'usuarios/visualizar.html', dicionarios)

def alterar(request):
    if not request.user.is_authenticated:
        return redirect('login')

    lista_Item = Estoque.objects.all()
    dicionarios = {"lista_Item": lista_Item}
    return render(request, 'usuarios/alterar.html', dicionarios)

def excluir_verificacao(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    lista_Item = Estoque.objects.get(pk=pk)
    dicionarios = {"lista_Item": lista_Item}
    return render(request, 'usuarios/excluir.html', dicionarios)

def excluir(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    item_selecionado = Estoque.objects.get(pk=pk)
    item_selecionado.delete()
    return redirect('alterar')

def editar_verificacao(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    lista_Item = Estoque.objects.get(pk=pk)
    dicionario_Item = {"lista_Item": lista_Item}
    return render(request, 'usuarios/editar.html', dicionario_Item)

def editar(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        nome = request.POST.get('nome')
        item = request.POST.get('item')
        quantidade = request.POST.get('quantidade')

        Estoque.objects.filter(pk=pk).update(
            nome=nome,
            item=item,
            quantidade=quantidade,
        )
        return redirect('alterar')
    else:
        return redirect('login')

def logout(request):
    if request.user.is_authenticated:
        logout_django(request)
        return redirect('login')
    else:
        return redirect('login')

def sobre(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/sobre.html')
    else:
        return redirect('login')

def contatos(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/contatos.html')
    else:
        return redirect('login')
