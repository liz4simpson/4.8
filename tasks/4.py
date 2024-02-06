#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
import math


def draw_house(canvas):
    # Рисуем дом
    canvas.create_rectangle(175, 150, 375, 300, fill="lightblue", outline="black")
    canvas.create_polygon(175, 150, 275, 50, 375, 150, fill="lightblue", outline="black")


def draw_sun(canvas):
    # Рисуем солнце
    canvas.create_oval(400, 50, 450, 100, fill="orange", outline="yellow")


def draw_grass(canvas):
    # Рисуем траву
    for i in range(10, 400, 20):
        y = 300 + 20 * math.sin(i / 40)  # Увеличиваем высоту травы
        canvas.create_line(i, 300, i + 10, y, fill="green")


def main():
    root = tk.Tk()
    root.title("Домик с солнцем и травой")

    canvas = tk.Canvas(root, width=500, height=400)
    canvas.pack()

    # Рисуем элементы
    draw_house(canvas)
    draw_sun(canvas)
    draw_grass(canvas)

    root.mainloop()


if __name__ == "__main__":
    main()