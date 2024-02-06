#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk


class ShoppingApp:
    def __init__(self, roote):
        self.root = roote
        self.root.title("Список покупок")

        # Список товаров
        self.available_items = ["Яблоко", "Банан", "Молоко", "Хлеб", "Яйца", "Сахар", "Чай", "Кофе"]

        # Список покупок
        self.shopping_list = []

        # Создаем Listbox для доступных товаров
        self.available_listbox = tk.Listbox(roote, selectmode=tk.MULTIPLE)
        for item in self.available_items:
            self.available_listbox.insert(tk.END, item)
        self.available_listbox.pack(padx=10, pady=10, side=tk.LEFT)

        # Создаем Listbox для списка покупок
        self.shopping_listbox = tk.Listbox(roote, selectmode=tk.MULTIPLE)
        self.shopping_listbox.pack(padx=10, pady=10, side=tk.RIGHT)

        # Кнопка для добавления товаров в список покупок
        self.add_button = tk.Button(roote, text="Добавить в покупки", command=self.add_to_shopping_list)
        self.add_button.pack(pady=10)

        # Кнопка для удаления товаров из списка покупок
        self.remove_button = tk.Button(roote, text="Убрать из покупок", command=self.remove_from_shopping_list)
        self.remove_button.pack(pady=20)

    def add_to_shopping_list(self):
        selected_items = list(self.available_listbox.curselection())
        selected_items.reverse()
        for index in selected_items:
            item = self.available_items[index]
            if item not in self.shopping_list:
                self.shopping_list.append(item)
                self.shopping_listbox.insert(tk.END, item)
                self.available_listbox.delete(index)

    def remove_from_shopping_list(self):
        selected_items = list(self.shopping_listbox.curselection())
        selected_items.reverse()
        for index in selected_items:
            item = self.shopping_list[index]
            self.shopping_list.remove(item)
            self.shopping_listbox.delete(index)
            self.available_listbox.insert(tk.END, item)


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root)
    root.mainloop()
