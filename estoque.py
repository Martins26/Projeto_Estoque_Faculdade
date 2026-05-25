from tkinter import *

estoque = {
    1: {"nome": "banana", "categoria": "fruta", "preco": 15.0, "quantidade": 21},
    2: {"nome": "pera", "categoria": "fruta", "preco": 2.0, "quantidade": 19}
}


def cadastrar_produtos(produto_id, nome, categoria, preco, quantidade):
    produtos = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    estoque[produto_id] = produtos
    print(f"Produto {nome} da categoria {categoria} cadastrado com sucesso!")


def registrar_entrada(produto_id, quantidade):
    if produto_id in estoque:
        estoque[produto_id]["quantidade"] += quantidade
        print(f"Adicionado {quantidade} unidades ao produto!")
    else:
        print("Produto não encontrado")


def registrar_saida(produto_id, quantidade):
    if produto_id in estoque:
        if estoque[produto_id]["quantidade"] >= quantidade:
            estoque[produto_id]["quantidade"] -= quantidade
            print(f"Removido {quantidade} unidades do produto!")
        else:
            print("Quantidade indisponível")
    else:
        print("Produto não encontrado")


def consultar_estoque(produto_id):
    if produto_id in estoque:
        produto = estoque[produto_id]

        print("\n=== DETALHES DO PRODUTO ===")
        print(f"Nome:       {produto['nome']}")
        print(f"Categoria:  {produto['categoria']}")
        print(f"Preço:      R$ {produto['preco']}")
        print(f"Quantidade: {produto['quantidade']} unidades")
        print("===========================")
    else:
        print("Produto não encontrado")


def alertar_estoque_baixo(limite):
    print("\n=== ALERTA DE ESTOQUE BAIXO ===")

    for produto_id, informacoes in estoque.items():
        if informacoes["quantidade"] < limite:
            print(
                f"O item {informacoes['nome']} "
                f"(ID: {produto_id}) tem apenas "
                f"{informacoes['quantidade']} unidades"
            )


cadastrar_produtos(3, "Cenoura", "verdura", 3.50, 15)

registrar_entrada(3, 15)

registrar_saida(3, 5)

consultar_estoque(1)

alertar_estoque_baixo(20)

janela = Tk()

janela.mainloop()