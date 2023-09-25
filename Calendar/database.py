database.py

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
