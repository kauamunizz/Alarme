import tkinter as tk
import datetime
import time
import os
from playsound import playsound


def alarme():
    while True:
        set_alarme = f'{hora.get()}:{minutos.get()}:{segundos.get()}'
        time.sleep(1)
        hora_local = datetime.datetime.now().strftime('%H:%M:%S')
        print(hora_local, set_alarme)
        
        if set_alarme == hora_local:
            print("Alarme disparado!")
            playsound("alarme_msc.mp3")
            break
            

janela = tk.Tk()

tk.Label(janela, text='Alarme em Python', font='Helvetica 18 bold').pack(pady=10)
tk.Label(janela, text='Definir alarme').pack(pady=5)

frame = tk.Frame(janela)
frame.pack()


def option(value):
    opt = tk.StringVar(janela)
    options = [str(i).zfill(2) for i in range(value)]
    opt.set(options[0])
    tk.OptionMenu(frame, opt, *options).pack(side=tk.LEFT)
    return opt

hora = option(24)
minutos = option(60)
segundos = option(60)

tk.Button(janela, text='Definir', font='Helvetica 10', command=alarme).pack(pady='20')

janela.title("Alarme em python")
janela.geometry("500x200+500+500")
janela.mainloop()