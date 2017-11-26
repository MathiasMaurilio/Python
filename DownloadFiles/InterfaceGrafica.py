from functools import partial
from tkinter import *

def bt_click(botoes):
    print(botoes["text"])
    lb["text"] = botoes["text"]
    lb["text"] = ed.get()

janela = Tk()
janela.title("Janela Principal")
janela["bg"] = "green"
janela["background"] = "green"

bt1 = Button(janela, width=20, text="Botão 1")
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=5, y=10)

bt2 = Button(janela, width=20, text="Botão 2")
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=5, y=40)

ed = Entry(janela)
ed.place(x=5, y=70)

lb = Label(janela, text="Fala Galera!!!")
lb.place(x=5, y=250)
lb["bg"] = "green"

#LarguraxAltura+DistanciaEsquerta+DistanciaTopo
janela.geometry("500x300+400+100")

janela.mainloop()
