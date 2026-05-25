from tkinter import *

estoque = {
    1: {"Nome": "Banana", "Categoria": "Fruta", "Preço": 15.0, "Quantidade": 21},
    2: {"Nome": "Pera", "Categoria": "Fruta", "Preço": 2.0, "Quantidade": 19}
}


def cadastrar_produtos(produto_id, nome, categoria, preco, quantidade):
    produtos = {
        "Nome": nome,
        "Categoria": categoria,
        "Preço": preco,
        "Quantidade": quantidade
    }

    estoque[produto_id] = produtos
    print(f"Produto {nome} da categoria {categoria} cadastrado com sucesso!")


def registrar_entrada(produto_id, quantidade):
    if produto_id in estoque:
        estoque[produto_id]["Quantidade"] += quantidade
        print(f"Adicionado {quantidade} unidades ao produto!")
    else:
        print("Produto não encontrado")


def registrar_saida(produto_id, quantidade):
    if produto_id in estoque:
        if estoque[produto_id]["Quantidade"] >= quantidade:
            estoque[produto_id]["Quantidade"] -= quantidade
            print(f"Removido {quantidade} unidades do produto!")
        else:
            print("Quantidade indisponível")
    else:
        print("Produto não encontrado")


def consultar_estoque(produto_id=None):
    if produto_id is None:
        texto = ""
        for pid, info in estoque.items():
            texto += (
                f"ID: {pid}\n"
                f"Nome: {info['Nome']}\n"
                f"Categoria: {info['Categoria']}\n"
                f"Preço: R$ {info['Preço']}\n"
                f"Quantidade: {info['Quantidade']}\n"
                "------------------------\n"
            )
        return texto
    elif produto_id in estoque:
        produto = estoque[produto_id]
        texto = (
            f"Nome: {produto['Nome']}\n"
            f"Categoria: {produto['Categoria']}\n"
            f"Preço: R$ {produto['Preço']}\n"
            f"Quantidade: {produto['Quantidade']}"
        )

        return texto

    else:
        return "Produto não encontrado"


def alertar_estoque_baixo(limite):
    mensagem = "=== ALERTA DE ESTOQUE BAIXO ===\n"
    encontrou = False

    for produto_id, informacoes in estoque.items():
        if informacoes["Quantidade"] < limite:

            mensagem += (
                f"{informacoes['Nome']} "
                f"(ID: {produto_id}) possui apenas "
                f"{informacoes['Quantidade']} unidades restantes.\n"
            )

            encontrou = True

    if not encontrou:
        mensagem += "Nenhum produto com estoque baixo"

    return mensagem

def mostrar_estoque():
    texto_estoque["text"] = consultar_estoque()


cadastrar_produtos(3, "Cenoura", "Verdura", 3.50, 15)

registrar_entrada(3, 15)

registrar_saida(3, 5)

consultar_estoque()

alertar_estoque_baixo(20)


janela = Tk()
janela.title("Sistema de Controle de Estoque")
janela.geometry("400x400")

texto_orientacao = Label(janela, text="Bem-vindo ao Sistema de Controle de Estoque!")
texto_orientacao.grid(column=0, row=0, padx=70)
botao = Button(janela, text="Clique aqui para ver o estoque", command= mostrar_estoque)
botao.grid(column=0, row=1, pady=10)
texto_estoque = Label(janela, text="")
texto_estoque.grid(column=0, row=2)
texto_alerta = Label(janela, text=alertar_estoque_baixo(20))
texto_alerta.grid(column=0, row=3)


janela.mainloop()