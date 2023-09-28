import sqlite3 # Importando o banco de dados sqlite
import tkinter as tk # Importando a interface tkinter e chamando ela de tk para facilitar 
from tkinter import ttk # Importando uma parte da biblioteca tkinter chamada ttk que oferece algumas caracteristicas visuais
from tkcalendar import Calendar  # Adicionando o tkcalendar, para fazer a função de chamada do calendário e assim poder mostrar ou não o calendário

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect("BetterYou.db") # Estabelece uma conexão com o banco de dados ou o cria se não existir
cursor = conn.cursor() # Cria um cursor para executar comandos SQL

# Criar a tabela de tarefas se não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY,
        tipo TEXT,
        data TEXT,
        tarefa TEXT
    )
""")
conn.commit() # Confirma as alterações no banco de dados

# Função para adicionar tarefa ao banco de dados
def adicionar_tarefa():
    tipo = tipo_var.get()  # Obtém o tipo da tarefa do Combobox
    data = data_entry.get()  # Obtém a data inserida pelo usuário
    tarefa = tarefa_entry.get()  # Obtém a tarefa inserida pelo usuário
    
    cursor.execute("INSERT INTO tarefas (tipo, data, tarefa) VALUES (?, ?, ?)", (tipo, data, tarefa))  # Insere os dados no banco de dados
    conn.commit()  # Confirma a inserção
    
    listar_tarefas()  # Atualiza a lista de tarefas na interface

# Função para listar tarefas na interface
def listar_tarefas():
    for row in tree.get_children():
        tree.delete(row)  # Limpa a lista de tarefas
    
    cursor.execute("SELECT data, tarefa FROM tarefas WHERE tipo=?", (tipo_var.get(),))  # Obtém as tarefas do banco de dados
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)  # Insere as tarefas na lista da interface

# Função para mostrar o calendário (ainda não implementado= implementado/ falta ainda fazer com que as tarefas criadas sejam mostradas nele)
def mostrar_calendario():
    # Implemente a exibição do calendário aqui
    pass

# Função para fechar a janela e encerrar a conexão com o banco de dados
def fechar_janela():
    conn.close()  # Fecha a conexão com o banco de dados
    root.destroy()  # Fecha a janela da interface

# Função para mostrar o calendário
def mostrar_calendario():
    top = tk.Toplevel(root)  # Cria uma nova janela (top)
    cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1", year=2023, month=9, day=25)  # Cria um widget de calendário
    cal.pack(fill="both", expand=True)  # Empacota o widget para ocupar todo o espaço disponível
    ttk.Button(top, text="Selecionar Data", command=lambda: selecionar_data(cal.get_date())).pack()  # Cria um botão para selecionar a data

# Função para selecionar a data e inseri-la no Entry de Data
def selecionar_data(data):
    data_entry.delete(0, tk.END)  # Limpa a entrada de data
    data_entry.insert(0, data)  # Insere a data selecionada na entrada de data

# Criar a janela principal
root = tk.Tk()  # Cria a janela principal
root.title("BetterYou")  # Define o título da janela

# Tipo de Lista (Estudos, Exercícios, etc.)
tipo_var = tk.StringVar(root)  # Cria uma variável de controle para o Combobox
tipo_var.set("Estudos")  # Define o valor padrão
tipo_menu = ttk.Combobox(root, textvariable=tipo_var, values=["Estudos", "Exercícios", "Outros"])  # Cria o Combobox
tipo_menu.pack()  # Empacota o Combobox na interface

# Lista de Tarefas
tree = ttk.Treeview(root, columns=("Data", "Tarefa"), show="headings")  # Cria a lista de tarefas
tree.heading("Data", text="Data")  # Define o cabeçalho da coluna "Data"
tree.heading("Tarefa", text="Tarefa")  # Define o cabeçalho da coluna "Tarefa"
tree.pack()  # Empacota a lista na interface

# Entrada de Data e Tarefa
data_label = tk.Label(root, text="Data:")  # Cria um rótulo para a entrada de data
data_label.pack()  # Empacota o rótulo na interface
data_entry = tk.Entry(root)  # Cria a entrada de data
data_entry.pack()  # Empacota a entrada na interface

tarefa_label = tk.Label(root, text="Tarefa:")  # Cria um rótulo para a entrada de tarefa
tarefa_label.pack()  # Empacota o rótulo na interface
tarefa_entry = tk.Entry(root)  # Cria a entrada de tarefa
tarefa_entry.pack()  # Empacota a entrada na interface

# Botão para adicionar tarefa
adicionar_button = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa)  # Cria um botão para adicionar tarefas
adicionar_button.pack()  # Empacota o botão na interface

# Botão para mostrar o calendário (ainda não implementado)
mostrar_calendario_button = tk.Button(root, text="Mostrar Calendário", command=mostrar_calendario)  # Cria um botão para mostrar o calendário
mostrar_calendario_button.pack()  # Empacota o botão na interface

# Botão para fechar a janela
fechar_janela_button = tk.Button(root, text="Fechar", command=fechar_janela)  # Cria um botão para fechar a janela
fechar_janela_button.pack()  # Empacota o botão na interface

# Definindo funções para trabalhar com o banco de dados

def conectar_banco():
    conn = sqlite3.connect("BetterYou.db")  # Estabelece uma conexão com o banco de dados ou o cria se não existir
    cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY,
            tipo TEXT,
            data TEXT,
            tarefa TEXT
        )
    """)
    conn.commit()  # Confirma as alterações no banco de dados
    return conn  # Retorna a conexão para ser utilizada em outras partes do código

def adicionar_tarefa(conn, tipo, data, tarefa):
    cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
    cursor.execute("INSERT INTO tarefas (tipo, data, tarefa) VALUES (?, ?, ?)", (tipo, data, tarefa))  # Insere os dados no banco de dados
    conn.commit()  # Confirma a inserção

def obter_tarefas(conn, tipo):
    cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
    cursor.execute("SELECT data, tarefa FROM tarefas WHERE tipo=?", (tipo,))  # Obtém as tarefas do banco de dados
    return cursor.fetchall()  # Retorna as tarefas obtidas

# Listar tarefas iniciais
listar_tarefas()

# Iniciar a interface gráfica
root.protocol("WM_DELETE_WINDOW", fechar_janela)  # Define o comportamento ao fechar a janela
root.mainloop()  # Inicia o loop principal da interface gráfica


