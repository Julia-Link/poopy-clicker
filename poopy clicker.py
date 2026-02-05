#as lib
import pickle
import random
import tkinter as tk
from tkinter import ttk

#modulo de carregamento de save
def loada():
    with open("save.pkl", "rb") as load_file:
        global count
        global upg1
        global rnum
        upg1, count, rnum = pickle.load(load_file)
    label1.configure(text=f'você tem ${count}!')

#modulo de save
def save():
    with open("save.pkl", "wb") as save_file:
        pickle.dump([upg1, count, rnum], save_file)

#declarar variavel
count = 0
upg1 = 0
rnum = 1

#clicks
def clicked():
    global count
    global rnum

    count += rnum

    label1.configure(text=f'você tem ${count}!')

    if upg1 == 1:
        rnum = 2

    if upg1 == 2:
        rnum = 4

    if upg1 == 3:
        rnum = 8

    if upg1 == 4:
        rnum = 16

    if upg1 == 5:
        rnum = 32

    if upg1 == 6:
        rnum = 64

    if upg1 == 7:
        rnum = 128

    if upg1 == 8:
        rnum = 256

    if upg1 == 9:
        rnum = 512

    if upg1 == 10:
        rnum = 1024

#upgrades
def upgrade():
    global upg1
    global count

    if count >= 200:
        count = count - 200
        upg1 = 1

def upgrade2():
    global upg1
    global count

    if count >= 400:
        count = count - 400
        upg1 = 2

def upgrade3():
    global upg1
    global count

    if count >= 800:
        count = count - 800
        upg1 = 3

def upgrade4():
    global upg1
    global count

    if count >= 1600:
        count = count - 1600
        upg1 = 4

def upgrade5():
    global upg1
    global count

    if count >= 3200:
        count = count - 3200
        upg1 = 5

def upgrade6():
    global upg1
    global count

    if count >= 6400:
        count = count - 6400
        upg1 = 6


def upgrade7():
    global upg1
    global count

    if count >= 12800:
        count = count - 12800
        upg1 = 7

def upgrade8():
    global upg1
    global count

    if count >= 25600:
        count = count - 25600
        upg1 = 8

def upgrade9():
    global upg1
    global count

    if count >= 51200:
        count = count - 51200
        upg1 = 9

def upgrade10():
    global upg1
    global count

    if count >= 102400:
        count = count - 102400
        upg1 = 10

#criar janela nova
def janela():
    janela2 = tk.Toplevel()
    janela2.geometry("250x170")
    janela2.configure(background="#9a9a9a")
    janela2.resizable(width=False, height=False)
    custom_button = ttk.Button(janela2, text="2x | $200", command=upgrade)
    custom_button.place(x=0, y=0)
    custom_button = ttk.Button(janela2, text="4x | $400", command=upgrade2)
    custom_button.place(x=0, y=35)
    custom_button = ttk.Button(janela2, text="8x | $800", command=upgrade3)
    custom_button.place(x=0, y=70)
    custom_button = ttk.Button(janela2, text="16x | $1600", command=upgrade4)
    custom_button.place(x=0, y=105)
    custom_button = ttk.Button(janela2, text="32x | $3200", command=upgrade5)
    custom_button.place(x=0, y=140)
    custom_button = ttk.Button(janela2, text="64x | $6400", command=upgrade6)
    custom_button.place(x=132, y=0)
    custom_button = ttk.Button(janela2, text="128x | $12800", command=upgrade7)
    custom_button.place(x=132, y=35)
    custom_button = ttk.Button(janela2, text="256x | $25600", command=upgrade8)
    custom_button.place(x=132, y=70)
    custom_button = ttk.Button(janela2, text="512x | $51200", command=upgrade9)
    custom_button.place(x=132, y=105)
    custom_button = ttk.Button(janela2, text="1024x | $102400", command=upgrade10)
    custom_button.place(x=132, y=140)

#janela principal
windows = tk.Tk()
windows.title("poopy clicker")
windows.geometry("250x200")
windows.configure(background="#9a9a9a")
windows.resizable(width=False, height=False)

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="#9a9a9a")
style.configure("BG.TLabel", foreground="black", background="yellow")

#lable
label1 = tk.Label(windows)
label1.pack(side=tk.TOP)
label1.configure(background="#9a9a9a", text=f'você tem ${count}!', font=("Segoe UI Symbol", 15))

#jiggle physics
def jiggle():
    x = random.randint(0, 200)
    y = random.randint(50, 100)
    click.place(x=x, y=y)

#botão
click = ttk.Button(windows, text="click", command=lambda: [clicked(), jiggle()], style="BW.TLabel")
click.place(x=50, y=50, width=32, height=20)

#botão da loja
lojabotao = ttk.Button(windows, text="loja", command=janela, style="BG.TLabel")
lojabotao.pack(side=tk.BOTTOM)

#janela de save
def janelasave():
    janelasave = tk.Toplevel()
    janelasave.geometry("170x50")
    janelasave.configure(background="#9a9a9a")
    janelasave.resizable(width=False, height=False)
    savebotao = ttk.Button(janelasave, text="save", command=save)
    savebotao.pack(side=tk.RIGHT)
    loadbotao = ttk.Button(janelasave, text="load", command=loada)
    loadbotao.pack(side=tk.LEFT)

#botãokk
lojabotao = ttk.Button(windows, text="save/load", command=janelasave)
lojabotao.place(x=0, y=170,)

#pra janela ficar rodando
windows.mainloop()
