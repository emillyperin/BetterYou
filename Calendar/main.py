main.py

import tkinter as tk
from tkinter import ttk
from interface import mostrar_calendario
from Calendar.database import conectar_banco, adicionar_tarefa, obter_tarefas

def adicionar_tarefa_callback():
    tipo = tipo_var.get()
    data = data_entry.get()
    tarefa = tarefa_entry.get()
    
    adicionar_tarefa(conn, tipo, data, tarefa)
    listar_tarefas()

def listar_tarefas():
    for row in tree.get_children():
        tree.delete(row)
    
    tarefas = obter_tarefas(conn, tipo_var.get())
    for row in tarefas:
        tree.insert("", "end", values=row)

def selecionar_data(data, data_entry):
    data_entry.delete(0, tk.END)
    data_entry.insert(0, data)

def fechar_janela():
    conn.close()
    root.destroy()

# Criar a janela principal
root = tk.Tk()
root.title("Agenda")

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = conectar_banco()

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
adicionar_button = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa_callback)
adicionar_button.pack()

# Botão para mostrar o calendário
mostrar_calendario_button = tk.Button(root, text="Mostrar Calendário", command=lambda: mostrar_calendario(data_entry, selecionar_data))
mostrar_calendario_button.pack()

# Botão para fechar a janela
fechar_janela_button = tk.Button(root, text="Fechar", command=fechar_janela)
fechar_janela_button.pack()

# Listar tarefas iniciais
listar_tarefas()

# Iniciar a interface gráfica
root.protocol("WM_DELETE_WINDOW", fechar_janela)
root.mainloop()
