#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk


def on_enter(_):
    text = entry.get()
    if text:
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)


def on_double_click(_):
    selected_index = listbox.curselection()
    if selected_index:
        selected_text = listbox.get(selected_index)
        entry.delete(0, tk.END)
        entry.insert(0, selected_text)


root = tk.Tk()
root.title("Программа с полем ввода и списком")

entry = tk.Entry(root)
entry.pack(pady=10)
entry.bind("<Return>", on_enter)

listbox = tk.Listbox(root)
listbox.pack(expand=True, fill=tk.BOTH)
listbox.bind("<Double-Button-1>", on_double_click)

root.mainloop()
