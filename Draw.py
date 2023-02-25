from tkinter import *
from random import randint

h = 500
w = 500

root = Tk()

def draw_random_oval(x, y):
    canvas.create_oval(
        randint(0, x), 
        randint(0, y), 
        randint(0, x), 
        randint(0, y)
    )

def draw_random_rectangle(x, y):
    canvas.create_rectangle(
        randint(0, x), 
        randint(0, y), 
        randint(0, x), 
        randint(0, y),
    )

def draw_random_polygon(x, y):
    canvas.create_polygon(
        randint(0, x), 
        randint(0, y), 
        randint(0, x), 
        randint(0, y),         
        randint(0, x), 
        randint(0, y),
    )

def draw():
    global w, h, is_figure
    canvas.delete('all')
    f_type = randint(0,2)
    if f_type == 0:
        draw_random_oval(w, h)
    elif f_type == 1:
        draw_random_rectangle(w, h)
    else:
        draw_random_polygon(w, h)

canvas = Canvas(root, width=w, height=h, background='white')
canvas.pack()

b1 = Button(text='Button', command=draw)
b1.pack()

root.mainloop()
