from math import sqrt
from tkinter import ttk
import tkinter as tk


class Matematicando:
    @staticmethod
    def __adicionar():
        lista = []
        for c in range(1, 1001):
            lista.append(c)
        return lista

    def __init__(self):
        self.numero = None
        self.raiz = None
        self.divisores = []
        self.primo = None
        self.numeros_disponiveis = self.__adicionar()
        self.texto = ''

    def calcular_divisores(self):
        for c in range(self.numero, 0, -1):
            if self.numero % c == 0:
                self.divisores.append(c)

    def mostrar_divisores(self):
        self.calcular_divisores()
        mensagem_divisores['text'] = f'Os divisores de {self.numero}\n são {self.divisores}'

    def e_primo_ou_nao(self):
        if len(self.divisores) == 2:
            self.primo = 'É PRIMO'
        else:
            self.primo = 'NÃO É PRIMO'

    def mostrar_primo(self):
        self.e_primo_ou_nao()
        mensagem_primo['text'] = f'O número {self.numero}\n {self.primo}'

    def calcular_raiz(self):
        self.raiz = sqrt(self.numero)

    def mostrar_raiz(self):
        self.calcular_raiz()
        mensagem_raiz['text'] = f'A raiz quadrada de {self.numero} é {self.raiz:.1f}'

    def mat(self):
        try:
            self.divisores.clear()
            num = escolha.get()
            num = int(num)
            self.numero = num
            self.mostrar_divisores()
            self.mostrar_primo()
            self.mostrar_raiz()
            mensagem['fg'] = '#FFB6C1'
            mensagem['text'] = f'Número alterado para\n {self.numero} com sucesso!'
        except:
            mensagem['fg'] = 'red'
            mensagem['text'] = 'Erro, digite o que se pede!'


mate = Matematicando()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFE4E1')

titulo = tk.Label(text='Matematica', borderwidth=4, relief='raised', bg='#FFB6C1', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Escolha um número aqui ->', bg='#FFE4E1', fg='#FFB6C1', font='Arial 10 bold')
mensagem.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=mate.numeros_disponiveis)
escolha.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Divisores', borderwidth=4, relief='raised', bg='#FFB6C1', fg='white',
                   font='Arial 12 bold')
titulo2.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

mensagem_divisores = tk.Label(text='Divisores do número...', bg='#FFE4E1', fg='#FFB6C1', font='Arial 10 bold')
mensagem_divisores.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

titulo3 = tk.Label(text='Primo ou não?', borderwidth=4, relief='raised', bg='#FFB6C1', fg='white',
                   font='Arial 12 bold')
titulo3.grid(row=2, column=2, columnspan=2, padx=10, pady=10, sticky='nswe')

mensagem_primo = tk.Label(text='Primo ou não primo?', bg='#FFE4E1', fg='#FFB6C1', font='Arial 10 bold')
mensagem_primo.grid(row=3, column=2, columnspan=2, padx=10, pady=10, sticky='nswe')

titulo4 = tk.Label(text='Raiz Quadrada', borderwidth=4, relief='raised', bg='#FFB6C1', fg='white',
                   font='Arial 12 bold')
titulo4.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

mensagem_raiz = tk.Label(text='Raiz quadrada do número', bg='#FFE4E1', fg='#FFB6C1', font='Arial 10 bold')
mensagem_raiz.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_numero = tk.Button(text='Mudar número', bg='#FFB6C1', fg='white', font='Arial 13 bold',
                               command=mate.mat)
botao_mudar_numero.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
