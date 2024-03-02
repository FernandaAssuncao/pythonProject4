from random import choice
import tkinter as tk
from tkinter import ttk


class Jokenpo:
    def __init__(self):
        self.usuario = 'pedra'
        self.computador = None
        self.vencedor = ''
        self.lista_opcoes = ['pedra',
                             'papel',
                             'tesoura']

    def escolha_usuario(self):
        if self.usuario in self.lista_opcoes:
            self.usuario = mudar_usuario.get()
            self.computador = choice(self.lista_opcoes)
            self.__escolhas()
            self.mostrar_vencedor()
        else:
            mostrar_escolhas['foreground'] = 'red'
            mostrar_escolhas['text'] = 'Erro,digite uma\ndas opções acima!'

    def __escolhas(self):
        mostrar_escolhas['text'] = f'Você escolheu: {self.usuario}\ncomputador escolheu: {self.computador}'

    def verificar_escolhas(self):
        if (self.usuario == 'pedra') and (self.computador == 'pedra'):
            self.vencedor = 'empate'
        elif (self.usuario == 'pedra') and (self.computador == 'papel'):
            self.vencedor = 'computador'
        elif (self.usuario == 'pedra') and (self.computador == 'tesoura'):
            self.vencedor = 'você'
        elif (self.usuario == 'papel') and (self.computador == 'pedra'):
            self.vencedor = 'você'
        elif (self.usuario == 'papel') and (self.computador == 'papel'):
            self.vencedor = 'empate'
        elif (self.usuario == 'papel') and (self.computador == 'tesoura'):
            self.vencedor = 'computador'
        elif (self.usuario == 'tesoura') and (self.computador == 'pedra'):
            self.vencedor = 'computador'
        elif (self.usuario == 'tesoura') and (self.computador == 'papel'):
            self.vencedor = 'você'
        elif (self.usuario == 'tesoura') and (self.computador == 'tesoura'):
            self.vencedor = 'empate'

    def mostrar_vencedor(self):
        self.verificar_escolhas()
        mensagem_vencedor['text'] = f'O vencedor foi {self.vencedor}'


jogo = Jokenpo()
janela = tk.Tk()
janela.title('Jokenpo')
janela.configure(background='black')

titulo = tk.Label(text='Jogo Jokenpo', borderwidth=4, relief='ridge', background='pink', foreground='purple')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem1 = tk.Label(text='Pedra,papel e tesoura?', foreground='pink', background='black')
mensagem1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

mudar_usuario = ttk.Combobox(values=jogo.lista_opcoes)
mudar_usuario.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mostrar_escolhas = tk.Label(text='', background='black', foreground='pink')
mostrar_escolhas.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_jogar = tk.Button(text='Jogar', background='pink', foreground='purple', command=jogo.escolha_usuario)
botao_jogar.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Vencedor', borderwidth=4, relief='ridge', background='pink', foreground='purple')
titulo2.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem_vencedor = tk.Label(text='', foreground='pink', background='black')
mensagem_vencedor.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar jogo', background='pink', foreground='purple', command=janela.quit)
botao_fechar.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
