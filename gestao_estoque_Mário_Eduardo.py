from tkinter import *
from tkinter import messagebox

estoque = {
    1: {"Nome": "Banana", "Categoria": "Fruta", "Preço": 15.0, "Quantidade": 21},
    2: {"Nome": "Pera", "Categoria": "Fruta", "Preço": 2.0, "Quantidade": 19}
}


def cadastrar_produtos(produto_id, nome, categoria, preco, quantidade):
    """Registra novo produto no sistema"""

    produtos = {
        "Nome": nome,
        "Categoria": categoria,
        "Preço": preco,
        "Quantidade": quantidade
    }

    estoque[produto_id] = produtos

    atualizar_alerta()

    messagebox.showinfo(
        "Produto cadastrado",
        f"Produto {nome} cadastrado com sucesso!"
    )


def registrar_entrada(produto_id, quantidade):
    """Adiciona itens ao estoque"""

    if produto_id in estoque:

        estoque[produto_id]["Quantidade"] += quantidade

        atualizar_alerta()

        messagebox.showinfo(
            "Entrada Registrada",
            f"Adicionado {quantidade} unidades ao produto {estoque[produto_id]['Nome']}!"
        )

    else:

        messagebox.showerror(
            "Produto não encontrado",
            "O produto especificado não foi encontrado."
        )


def registrar_saida(produto_id, quantidade):
    """Remove itens do estoque"""

    if produto_id in estoque:

        if estoque[produto_id]["Quantidade"] >= quantidade:

            estoque[produto_id]["Quantidade"] -= quantidade

            atualizar_alerta()

            messagebox.showinfo(
                "Saída Registrada",
                f"Removido {quantidade} unidades do produto {estoque[produto_id]['Nome']}!"
            )

        else:

            messagebox.showerror(
                "Quantidade insuficiente",
                "A quantidade solicitada não está disponível em estoque."
            )

    else:

        messagebox.showerror(
            "Produto não encontrado",
            "O produto especificado não foi encontrado."
        )


def consultar_estoque(produto_id=None):
    """Verifica saldo atual do produto"""

    if produto_id is None:

        texto = ""

        for pid, info in estoque.items():

            texto += (
                f"ID: {pid}\n"
                f"Nome: {info['Nome']}\n"
                f"Categoria: {info['Categoria']}\n"
                f"Preço: R$ {info['Preço']:.2f}\n"
                f"Quantidade: {info['Quantidade']}\n"
                "------------------------\n"
            )

        return texto

    elif produto_id in estoque:

        produto = estoque[produto_id]

        texto = (
            f"Nome: {produto['Nome']}\n"
            f"Categoria: {produto['Categoria']}\n"
            f"Preço: R$ {produto['Preço']:.2f}\n"
            f"Quantidade: {produto['Quantidade']}"
        )

        return texto

    else:

        return "Produto não encontrado"


def alertar_estoque_baixo(limite):
    """Identifica produtos com estoque crítico"""

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


def atualizar_alerta():

    texto_alerta["text"] = alertar_estoque_baixo(20)


def mostrar_estoque():

    texto_estoque["text"] = consultar_estoque()


def pegar_dados():

    try:

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

        entry_id.delete(0, END)
        entry_nome.delete(0, END)
        entry_categoria.delete(0, END)
        entry_preco.delete(0, END)
        entry_quantidade.delete(0, END)

    except:

        messagebox.showerror(
            "Erro",
            "Digite valores válidos!"
        )


def pegar_entrada():

    try:

        produto_id = int(entry_mov_id.get())
        quantidade = int(entry_mov_quantidade.get())

        registrar_entrada(produto_id, quantidade)

        mostrar_estoque()

        entry_mov_id.delete(0, END)
        entry_mov_quantidade.delete(0, END)

    except:

        messagebox.showerror(
            "Erro",
            "Digite valores válidos!"
        )


def pegar_saida():

    try:

        produto_id = int(entry_mov_id.get())
        quantidade = int(entry_mov_quantidade.get())

        registrar_saida(produto_id, quantidade)

        mostrar_estoque()

        entry_mov_id.delete(0, END)
        entry_mov_quantidade.delete(0, END)

    except:

        messagebox.showerror(
            "Erro",
            "Digite valores válidos!"
        )


janela = Tk()
janela.title("Sistema de Controle de Estoque")
janela.geometry("1280x720")

canvas = Canvas(janela)

scrollbar = Scrollbar(
    janela,
    orient=VERTICAL,
    command=canvas.yview
)

scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window(
    (0, 0),
    window=scrollable_frame,
    anchor="nw"
)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar.pack(side=RIGHT, fill=Y)


def scroll_mouse(event):

    canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


canvas.bind_all("<MouseWheel>", scroll_mouse)

texto_orientacao = Label(
    scrollable_frame,
    text="Bem-vindo ao Sistema de Controle de Estoque!",
    font=("Arial", 28)
)

texto_orientacao.grid(
    row=0,
    column=0,
    pady=30,
    padx=200
)

texto_orientacao2 = Label(
    scrollable_frame,
    text="Preencha as informações abaixo para cadastrar um novo produto:",
    font=("Arial", 16)
)

texto_orientacao2.grid(
    row=1,
    column=0,
    pady=10
)

frame_formulario = Frame(scrollable_frame)

frame_formulario.grid(
    row=2,
    column=0,
    pady=20
)

Label(
    frame_formulario,
    text="ID:",
    font=("Arial", 12)
).grid(
    row=0,
    column=0,
    sticky="w",
    pady=5
)

entry_id = Entry(frame_formulario)

entry_id.grid(
    row=0,
    column=1,
    padx=10
)

Label(
    frame_formulario,
    text="Nome:",
    font=("Arial", 12)
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=5
)

entry_nome = Entry(frame_formulario)

entry_nome.grid(
    row=1,
    column=1,
    padx=10
)

Label(
    frame_formulario,
    text="Categoria:",
    font=("Arial", 12)
).grid(
    row=2,
    column=0,
    sticky="w",
    pady=5
)

entry_categoria = Entry(frame_formulario)

entry_categoria.grid(
    row=2,
    column=1,
    padx=10
)

Label(
    frame_formulario,
    text="Preço:",
    font=("Arial", 12)
).grid(
    row=3,
    column=0,
    sticky="w",
    pady=5
)

entry_preco = Entry(frame_formulario)

entry_preco.grid(
    row=3,
    column=1,
    padx=10
)

Label(
    frame_formulario,
    text="Quantidade:",
    font=("Arial", 12)
).grid(
    row=4,
    column=0,
    sticky="w",
    pady=5
)

entry_quantidade = Entry(frame_formulario)

entry_quantidade.grid(
    row=4,
    column=1,
    padx=10
)

botao_cadastrar = Button(
    frame_formulario,
    text="Cadastrar Produto",
    command=pegar_dados
)

botao_cadastrar.grid(
    row=5,
    column=0,
    columnspan=2,
    pady=20
)

texto_movimentacao = Label(
    scrollable_frame,
    text="Registrar Entrada / Saída",
    font=("Arial", 18)
)

texto_movimentacao.grid(
    row=3,
    column=0,
    pady=20
)

frame_movimentacao = Frame(scrollable_frame)

frame_movimentacao.grid(
    row=4,
    column=0,
    pady=10
)

Label(
    frame_movimentacao,
    text="ID Produto:",
    font=("Arial", 12)
).grid(
    row=0,
    column=0,
    pady=5,
    sticky="w"
)

entry_mov_id = Entry(frame_movimentacao)

entry_mov_id.grid(
    row=0,
    column=1,
    padx=10
)

Label(
    frame_movimentacao,
    text="Quantidade:",
    font=("Arial", 12)
).grid(
    row=1,
    column=0,
    pady=5,
    sticky="w"
)

entry_mov_quantidade = Entry(frame_movimentacao)

entry_mov_quantidade.grid(
    row=1,
    column=1,
    padx=10
)

botao_entrada = Button(
    frame_movimentacao,
    text="Adicionar Estoque",
    command=pegar_entrada,
    bg="lightgreen"
)

botao_entrada.grid(
    row=2,
    column=0,
    pady=15,
    padx=10
)

botao_saida = Button(
    frame_movimentacao,
    text="Remover Estoque",
    command=pegar_saida,
    bg="#ff9999"
)

botao_saida.grid(
    row=2,
    column=1,
    pady=15,
    padx=10
)

botao_estoque = Button(
    scrollable_frame,
    text="Clique aqui para ver o estoque",
    command=mostrar_estoque
)

botao_estoque.grid(
    row=5,
    column=0,
    pady=10
)

texto_estoque = Label(
    scrollable_frame,
    text="",
    justify=LEFT,
    font=("Arial", 11)
)

texto_estoque.grid(
    row=6,
    column=0,
    pady=20
)

texto_alerta = Label(
    scrollable_frame,
    text=alertar_estoque_baixo(20),
    font=("Arial", 11),
    fg="red"
)

texto_alerta.grid(
    row=7,
    column=0,
    pady=10
)

janela.mainloop()