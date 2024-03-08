import tkinter as tk
from tkinter import ttk


class Divisores:
    @staticmethod
    def __adicionar_numeros_disponiveis():
        lista = []
        for c in range(1, 1001):
            lista.append(c)
        return lista

    def __init__(self):
        self.numero = None
        self.divisores = []
        self.texto = ''
        self.numeros_disponiveis = self.__adicionar_numeros_disponiveis()

    def excluir_divisores(self):
        if len(self.divisores) != 0:
            self.divisores.clear()
            self.texto = ''

    def calcular(self):
        for c in range(1, self.numero + 1):
            if self.numero % c == 0:
                self.divisores.append(c)

    def mudar_mensagem(self):
        self.mudar_mensagem_numero()
        for div in self.divisores:
            self.texto = self.texto + f'{div}, '

    def mudar_mensagem_numero(self):
        self.texto = f'Os divisores de {self.numero} são\n '

    def finalizacao_mensagem(self):
        aviso['fg'] = 'white'
        aviso['text'] = self.texto

    def mostrar_divisores(self):
        try:
            self.excluir_divisores()
            num = numero.get()
            num = int(num)
            self.numero = num
            self.calcular()
            self.mudar_mensagem()
            self.finalizacao_mensagem()
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro,digite um valor valido!!'


divisores = Divisores()
janela = tk.Tk()
janela.title()
janela.configure(bg="#FFC0CB")

titulo = tk.Label(text='Digite um numero para\n ver seus divisores', borderwidth=2,
                  relief='raised', bg='#FFB6C1', fg="white", font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Digite um número aqui\n para saber seus divisores', bg='#FFC0CB',
                    fg='white', font='Arial 10 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

numero = ttk.Combobox(values=divisores.numeros_disponiveis)
numero.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFC0CB', fg='white', font='Arial 12 bold')
aviso.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_calcular_divisores = tk.Button(text='Calcular Divisores', bg='#FFB6C1',
                                     fg='white', font='Arial 13 bold', command=divisores.mostrar_divisores)
botao_calcular_divisores.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
