from django.shortcuts import render

from codingdojo.entity import Produto

produtos = (
    Produto(id=1, nome='Relogio Adidas', valor=30.00, quantidade=5, descricao='Relogio Adidas'),
    Produto(id=2, nome='Relogio Nike', valor=30.00, quantidade=2, descricao='Relogio Nike'),
    Produto(id=3, nome='Relogio do Avô', valor=300.00, quantidade=1, descricao='Relogio Guerra')
)


def produto(request):
    return render(request, 'index.html', {'lista': produtos})


def ver_produto(request, id:int):
    for produto in produtos:
        if produto.id == id:
            return render(request, "produtos.html", {"produto": produto})


def adicionar_produto(request):
    if request.method == "GET":
        return render(request, "adicionar.html")
    elif request.method == "POST":
        pass


def deletar_produto(request, id:int):
    print(request.method)
    if request.method == 'DELETE':
        for produto in produtos:
            if produto.id == id:
                return render(request, "index.html", {"lista": produtos, "msg":"Produto deletado."})
        return render(request, "index.html", {"lista": produtos, "msg":"Produto não encontrado."})
