import tkinter as tk
from tkinter import ttk


class Divisores:
    def __init__(self):
        self.numero = None
        self.texto_divisores = ''
        self.divisores = []
        self.numeros_disponiveis = [1, 2,
                                    3, 4,
                                    5, 6,
                                    7, 8,
                                    9, 10]

    def mostrar_divisores(self):
        mensagem['foreground'] = 'pink'
        mensagem['text'] = self.texto_divisores

    def quais_divisores(self):
        try:
            if len(self.divisores) != 0:
                self.divisores.clear()
            nume = num.get()
            self.numero = int(nume)
            for c in range(self.numero, 0, -1):
                if self.numero % c == 0:
                    self.divisores.append(c)
            self.texto_divisores = f'Divisores de {self.numero}: {self.divisores}'
            self.mostrar_divisores()
        except:
            mensagem['foreground'] = 'red'
            mensagem['text'] = 'Número invalido'


div = Divisores()
janela = tk.Tk()
janela.configure(bg='black')
janela.title('Divisores')

titulo = tk.Label(text='Digite um número para ver seus divisores', borderwidth=2,
                  relief='raised', background='pink')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

texto = tk.Label(text='Digite um número aqui', foreground='pink', background='black')
texto.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

num = ttk.Combobox(values=div.numeros_disponiveis, foreground='black')
num.grid(row=1, column=3, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='', background='black')
mensagem.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='nswe')

botao = tk.Button(text='Ver divisores', command=div.quais_divisores, bg='pink')
botao.grid(row=2, column=3, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar', command=janela.quit, bg='pink')
botao_fechar.grid(row=3, column=3, padx=10, pady=10, sticky='nswe')

janela.mainloop()
