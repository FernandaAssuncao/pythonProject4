from random import randint
from tkinter import ttk
import tkinter as tk


class JogoDoDado:
    @staticmethod
    def __adicionar_numero():
        lista = []
        for c in range(1, 7):
            lista.append(c)
        return lista

    def __init__(self):
        self.dado = None
        self.chute = None
        self.pontos = 0
        self.passou = False
        self.escolhas_disponiveis = self.__adicionar_numero()

    def girar_dado(self):
        self.dado = randint(1, 6)
        mensagem['text'] = 'Dado caiu!!'

    def adicionar_pontos(self):
        self.pontos += 1
        pontoss['text'] = f'Total de pontos: {self.pontos}'

    def verificar_resposta(self):
        if self.dado == self.chute:
            mensagem_final['text'] = f'Parabens você acertou!!\nO número que caiu no dado foi {self.dado}\nDado girado novamente!'
            self.adicionar_pontos()
        else:
            mensagem_final['text'] = f'Você errou!'

    def jogar(self):
        try:
            num = escolha.get()
            num = int(num)
            if num in self.escolhas_disponiveis:
                self.chute = num
                self.verificar_resposta()
            else:
                raise
        except:
            mensagem_final['fg'] = 'red'
            mensagem_final['text'] = 'Erro, faça o que se pede!'


jogo = JogoDoDado()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFC0CB')

titulo = tk.Label(text='Jogo do\n dado', borderwidth=4, relief='raised', bg='#FFB6C1',
                  fg='white', font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

pontoss = tk.Label(text='Total de pontos: 0', bg='#FFC0CB', fg='white', font='Arial 15 bold')
pontoss.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='', bg='#FFC0CB', fg='white', font='Arial 10 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_girar_dado = tk.Button(text='Girar Dado', bg='#FFB6C1', fg='white',
                             font='Arial 12 bold', command=jogo.girar_dado)
botao_girar_dado.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

mensagem2 = tk.Label(text='Digite o número que você\n acha que caiu no dado', bg='#FFC0CB',
                     fg='white', font='Arial 10 bold')
mensagem2.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=jogo.escolhas_disponiveis)
escolha.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

mensagem_final = tk.Label(text='', bg='#FFB6C1', fg='white', font='Arial 12 bold')
mensagem_final.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_tentar = tk.Button(text='Tentar', bg='#FFB6C1', fg='white', font='Arial 12 bold', command=jogo.jogar)
botao_tentar.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
