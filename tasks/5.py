#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *


def motion(event):
    current_x, current_y = c.coords(ball)[:2]
    target_x, target_y = event.x, event.y

    step_x = 1 if target_x > current_x else -1
    step_y = 1 if target_y > current_y else -1

    c.move(ball, step_x, step_y)

    if (step_x > 0 and current_x < target_x) or (step_x < 0 and current_x > target_x) or \
            (step_y > 0 and current_y < target_y) or (step_y < 0 and current_y > target_y):
        root.after(10, motion, event)


def on_click(event):
    motion(event)


root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()

ball = c.create_oval(0, 100, 40, 140, fill='green')

c.bind("<Button-1>", on_click)

root.mainloop()