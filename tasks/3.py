#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk


def on_button_click():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        text.config(width=width, height=height)
    except ValueError:
        pass


def on_focus_in(_):
    text.config(bg="white")


def on_focus_out(_):
    text.config(bg="lightgrey")


# Создаем главное окно
root = tk.Tk()
root.title("Изменение размеров текстового поля")

# Создаем текстовые поля для ввода размеров
width_label = tk.Label(root, text="Ширина:")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

height_label = tk.Label(root, text="Высота:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Создаем кнопку для изменения размеров
button = tk.Button(root, text="Изменить размер", command=on_button_click)
button.pack(pady=10)
button.bind("<Return>", lambda event: on_button_click())

# Создаем текстовое поле
text = tk.Text(root, bg="lightgrey")
text.pack(padx=10, pady=10)

# Привязываем события фокуса
text.bind("<FocusIn>", on_focus_in)
text.bind("<FocusOut>", on_focus_out)

# Запускаем главный цикл обработки событий
root.mainloop()
