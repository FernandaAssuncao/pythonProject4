from random import randint
from tkinter import ttk
import tkinter as tk


class JogoDoDado:
    @staticmethod
    def __adicionar_numeros(num=6):
        lista = []
        for c in range(1, num + 1):
            lista.append(c)
        return lista

    def __init__(self):
        self.dado = None
        self.palpite_usuario = None
        self.palpite_computador = None
        self.numeros_disponiveis = self.__adicionar_numeros(num=6)


jogo = JogoDoDado()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFEBCD')

titulo = tk.Label(text='Jogo do Dado', borderwidth=4, relief='raised', bg='#FFE4C4',
                  fg='white', font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

janela.mainloop()
