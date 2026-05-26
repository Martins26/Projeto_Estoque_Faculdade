from tkinter import *
from tkinter import messagebox

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
    messagebox.showinfo(
    "Produto cadastrado",
    f"Produto {nome} cadastrado com sucesso!"
)


def registrar_entrada(produto_id, quantidade):
    if produto_id in estoque:
        estoque[produto_id]["Quantidade"] += quantidade
        messagebox.showinfo("Entrada Registrada", f"Adicionado {quantidade} unidades ao produto {estoque[produto_id]['Nome']}!")
    else:
        messagebox.showerror("Produto não encontrado", "O produto especificado não foi encontrado.")


def registrar_saida(produto_id, quantidade):
    if produto_id in estoque:
        if estoque[produto_id]["Quantidade"] >= quantidade:
            estoque[produto_id]["Quantidade"] -= quantidade
            messagebox.showinfo("Saída Registrada", f"Removido {quantidade} unidades do produto {estoque[produto_id]['Nome']}!")
        else:
            messagebox.showerror("Quantidade insuficiente", "A quantidade solicitada não está disponível em estoque.")
    else:
        messagebox.showerror("Produto não encontrado", "O produto especificado não foi encontrado.")


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


def pegar_dados():

    produto_id = int(entry_id.get())
    nome = entry_nome.get()
    categoria = entry_categoria.get()
    preco = float(entry_preco.get())
    quantidade = int(entry_quantidade.get())

    cadastrar_produtos(
        produto_id,
        nome,
        categoria,
        preco,
        quantidade
    )

    mostrar_estoque()


cadastrar_produtos(3, "Cenoura", "Verdura", 3.50, 15)

registrar_entrada(3, 15)

registrar_saida(3, 5)

consultar_estoque()

alertar_estoque_baixo(20)


janela = Tk()
janela.title("Sistema de Controle de Estoque")
janela.geometry("1280x720")

texto_orientacao = Label(janela, text="Bem-vindo ao Sistema de Controle de Estoque!")
texto_orientacao.grid(column=0, row=0, padx=70)
texto_orientacao2 = Label(janela, text="Preencha as informações abaixo para cadastrar um novo produto:")
texto_orientacao2.grid(column=0, row=1, padx=70)
botao = Button(janela, text="Clique aqui para ver o estoque", command= mostrar_estoque)
botao.grid(column=0, row=10, pady=10)
texto_estoque = Label(janela, text="", justify=LEFT)
texto_estoque.grid(column=1, row=2, columnspan=2)
texto_alerta = Label(janela, text=alertar_estoque_baixo(20))
texto_alerta.grid(column=0, row=11)

Label(janela, text="ID").grid(column=0, row=4)
entry_id = Entry(janela)
entry_id.grid(column=1, row=4)

Label(janela, text="Nome").grid(column=0, row=5)
entry_nome = Entry(janela)
entry_nome.grid(column=1, row=5)

Label(janela, text="Categoria").grid(column=0, row=6)
entry_categoria = Entry(janela)
entry_categoria.grid(column=1, row=6)

Label(janela, text="Preço").grid(column=0, row=7)
entry_preco = Entry(janela)
entry_preco.grid(column=1, row=7)

Label(janela, text="Quantidade").grid(column=0, row=8)
entry_quantidade = Entry(janela)
entry_quantidade.grid(column=1, row=8)

botao_cadastrar = Button(
    janela,
    text="Cadastrar Produto",
    command=pegar_dados
)

botao_cadastrar.grid(column=0, row=9)


janela.mainloop()