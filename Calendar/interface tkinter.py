interface tkinter.py

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def mostrar_calendario(data_entry, selecionar_data):
    top = tk.Toplevel()
    cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1", year=2023, month=9, day=25)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="Selecionar Data", command=lambda: selecionar_data(cal.get_date(), data_entry)).pack()
