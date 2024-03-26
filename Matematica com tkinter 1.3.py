from math import sqrt
from tkinter import ttk
import tkinter as tk


class Matematicando:
    @staticmethod
    def __adicionar_numeros():
        lista = []
        for c in range(1, 2001):
            lista.append(c)
        return lista

    def __init__(self):
        self.numero = None
        self.divisores = []
        self.par_impar = None
        self.primo_ou_nao = None
        self.numeros_disponiveis = self.__adicionar_numeros()

    def mostrar_resultados(self):
        pass


mat = Matematicando()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFC0CB')

titulo = tk.Label(text='Matematica', borderwidth=4, relief='raised', bg='#FFB6C1', fg='white',
                  font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Digite aqui um número', bg='#FFC0CB', fg='white', font='Arial 12 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

numero = ttk.Combobox(values=mat.numeros_disponiveis)
numero.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFB6C1', fg='white', font='Arial 12 bold')
aviso.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_matematica = tk.Button(text='Obter informações', bg='#FFB6C1', fg='white',
                             font='Arial 15 bold', command=mat.mostrar_resultados)
botao_matematica.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
