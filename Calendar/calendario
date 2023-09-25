import sqlite3
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar  # Adicionando o tkcalendar

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect("BetterYou.db")
cursor = conn.cursor()

# Criar a tabela de tarefas se não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY,
        tipo TEXT,
        data TEXT,
        tarefa TEXT
    )
""")
conn.commit()

# Função para adicionar tarefa ao banco de dados
def adicionar_tarefa():
    tipo = tipo_var.get()
    data = data_entry.get()
    tarefa = tarefa_entry.get()
    
    cursor.execute("INSERT INTO tarefas (tipo, data, tarefa) VALUES (?, ?, ?)", (tipo, data, tarefa))
    conn.commit()
    
    listar_tarefas()

# Função para listar tarefas na interface
def listar_tarefas():
    for row in tree.get_children():
        tree.delete(row)
    
    cursor.execute("SELECT data, tarefa FROM tarefas WHERE tipo=?", (tipo_var.get(),))
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

# Função para mostrar o calendário (ainda não implementado= implementado/ falta ainda fazer com que as tarefas criadas sejam mostradas nele)
def mostrar_calendario():
    # Implemente a exibição do calendário aqui
    pass

# Função para fechar a janela e encerrar a conexão com o banco de dados
def fechar_janela():
    conn.close()
    root.destroy()

# Função para mostrar o calendário
def mostrar_calendario():
    top = tk.Toplevel(root)
    cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1", year=2023, month=9, day=25)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="Selecionar Data", command=lambda: selecionar_data(cal.get_date())).pack()

# Função para selecionar a data e inseri-la no Entry de Data
def selecionar_data(data):
    data_entry.delete(0, tk.END)
    data_entry.insert(0, data)

# Criar a janela principal
root = tk.Tk()
root.title("Agenda")

# Tipo de Lista (Estudos, Exercícios, etc.)
tipo_var = tk.StringVar(root)
tipo_var.set("Estudos")  # Valor padrão
tipo_menu = ttk.Combobox(root, textvariable=tipo_var, values=["Estudos", "Exercícios", "Outros"])
tipo_menu.pack()

# Lista de Tarefas
tree = ttk.Treeview(root, columns=("Data", "Tarefa"), show="headings")
tree.heading("Data", text="Data")
tree.heading("Tarefa", text="Tarefa")
tree.pack()

# Entrada de Data e Tarefa
data_label = tk.Label(root, text="Data:")
data_label.pack()
data_entry = tk.Entry(root)
data_entry.pack()

tarefa_label = tk.Label(root, text="Tarefa:")
tarefa_label.pack()
tarefa_entry = tk.Entry(root)
tarefa_entry.pack()

# Botão para adicionar tarefa
adicionar_button = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa)
adicionar_button.pack()

# Botão para mostrar o calendário (ainda não implementado)
mostrar_calendario_button = tk.Button(root, text="Mostrar Calendário", command=mostrar_calendario)
mostrar_calendario_button.pack()

# Botão para fechar a janela
fechar_janela_button = tk.Button(root, text="Fechar", command=fechar_janela)
fechar_janela_button.pack()

import sqlite3

def conectar_banco():
    conn = sqlite3.connect("BetterYou.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY,
            tipo TEXT,
            data TEXT,
            tarefa TEXT
        )
    """)
    conn.commit()
    return conn

def adicionar_tarefa(conn, tipo, data, tarefa):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (tipo, data, tarefa) VALUES (?, ?, ?)", (tipo, data, tarefa))
    conn.commit()

def obter_tarefas(conn, tipo):
    cursor = conn.cursor()
    cursor.execute("SELECT data, tarefa FROM tarefas WHERE tipo=?", (tipo,))
    return cursor.fetchall()


# Listar tarefas iniciais
listar_tarefas()

# Iniciar a interface gráfica
root.protocol("WM_DELETE_WINDOW", fechar_janela)
root.mainloop()