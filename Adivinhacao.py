from random import randint
from tkinter import ttk
import tkinter as tk


class JogoDaAdivinhacao:
    @staticmethod
    def __adicionar_numeros():
        lista = []
        for c in range(1, 11):
            lista.append(c)
        return lista

    def __init__(self):
        self.computador = None
        self.usuario = None
        self.escolhas_disponiveis = self.__adicionar_numeros()

    def computador_pensando(self):
        self.computador = randint(1, 10)
        mensagem['text'] = 'Já pensei, quero só\n vê você acertar em!?'

    def escolha_usuario(self):
        try:
            num = escolha.get()
            num = int(num)
            if num in self.escolhas_disponiveis:
                self.usuario = num
                if self.usuario == self.computador:
                    mensagem_acerto_erro['fg'] = 'white'
                    mensagem_acerto_erro['text'] = f'Parebens você acertou,\n eu pensei no número {self.computador}'
                else:
                    mensagem_acerto_erro['fg'] = 'white'
                    mensagem_acerto_erro['text'] = 'Errou, não\n foi esse número que pensei!'
            else:
                raise
        except:
            mensagem_acerto_erro['fg'] = 'red'
            mensagem_acerto_erro['text'] = 'Erro, por favor\n faça o que se pede!'


jogo = JogoDaAdivinhacao()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFEBCD')

titulo = tk.Label(text='Qual número que\n estou pensando?', borderwidth=4, relief='raised',
                  bg='#FFDAB9', fg='white',
                  font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='', bg='#FFDAB9', fg='white', font='Arial 10 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_pensar = tk.Button(text='Pedir para computador\n pensar em outro número', bg='#FFDAB9', fg='white',
                         font='Arial 12 bold', command=jogo.computador_pensando)
botao_pensar.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='Digite aqui o número que\n você acha que o computador pensou', bg='#FFEBCD',
                 fg='black', font='Arial 7 bold')
aviso.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=jogo.escolhas_disponiveis)
escolha.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

mensagem_acerto_erro = tk.Label(text='', bg='#FFDAB9', fg='white', font='Arial 15 bold')
mensagem_acerto_erro.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_tentar = tk.Button(text='Tentar', bg='#FFDAB9', fg='white',
                         font='Arial 12 bold', command=jogo.escolha_usuario)
botao_tentar.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
