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

#upgrades
def upgrade():
    global upg1
    global count

    if count >= 100:
        count = count - 100
        upg1 = 1

def upgrade2():
    global upg1
    global count

    if count >= 200:
        count = count - 200
        upg1 = 2

def upgrade3():
    global upg1
    global count

    if count >= 400:
        count = count - 400
        upg1 = 3

def upgrade4():
    global upg1
    global count

    if count >= 800:
        count = count - 800
        upg1 = 4

#criar janela nova
def janela():
    janela2 = tk.Toplevel()
    janela2.geometry("500x500")
    janela2.configure(background="#9a9a9a")
    janela2.resizable(width=False, height=False)
    custom_button = ttk.Button(janela2, text="2x | $100", command=upgrade)
    custom_button.place(x=0, y=0)
    custom_button = ttk.Button(janela2, text="4x | $200", command=upgrade2)
    custom_button.place(x=0, y=35)
    custom_button = ttk.Button(janela2, text="8x | $400", command=upgrade3)
    custom_button.place(x=0, y=70)
    custom_button = ttk.Button(janela2, text="16x | $800", command=upgrade4)
    custom_button.place(x=0, y=105)

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