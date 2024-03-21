from random import choice
from tkinter import ttk
import tkinter as tk


class Jokenpo:
    @staticmethod
    def __adicionar_escolhas():
        lista = ['pedra',
                 'papel',
                 'tesoura']
        return lista

    def __init__(self):
        self.escolha_usuario = None
        self.escolha_computador = None
        self.vencedor = ''
        self.escolhas_disponiveis = self.__adicionar_escolhas()

    def verificar_escolha_computador(self):
        self.escolha_computador = choice(self.escolhas_disponiveis)

    def analisar_escolha(self):
        if (self.escolha_usuario == 'pedra') and (self.escolha_computador == 'pedra'):
            self.vencedor = 'EMPATE!!'
        elif (self.escolha_usuario == 'pedra') and (self.escolha_computador == 'papel'):
            self.vencedor = 'COMPUTADOR'
        elif (self.escolha_usuario == 'pedra') and (self.escolha_computador == 'tesoura'):
            self.vencedor = 'VOCÊ'
        elif (self.escolha_usuario == 'papel') and (self.escolha_computador == 'pedra'):
            self.vencedor = 'VOCÊ'
        elif (self.escolha_usuario == 'papel') and (self.escolha_computador == 'papel'):
            self.vencedor = 'EMPATE'
        elif (self.escolha_usuario == 'papel') and (self.escolha_computador == 'tesoura'):
            self.vencedor = 'COMPUTADOR'
        elif (self.escolha_usuario == 'tesoura') and (self.escolha_computador == 'pedra'):
            self.vencedor = 'COMPUTADOR'
        elif (self.escolha_usuario == 'tesoura') and (self.escolha_computador == 'papel'):
            self.vencedor = 'VOCÊ'
        elif (self.escolha_usuario == 'tesoura') and (self.escolha_computador == 'tesoura'):
            self.vencedor = 'EMPATE'

    def mostrar_resultados(self):
        mensagem['fg'] = 'white'
        mensagem['text'] = f'Você escolheu {self.escolha_usuario}\nO computador escolheu {self.escolha_computador}\nVecedor: {self.vencedor}'

    def iniciar_jogo(self):
        try:
            escolhi = escolha.get()
            if escolhi in self.escolhas_disponiveis:
                self.escolha_usuario = str(escolhi)
                self.verificar_escolha_computador()
                self.analisar_escolha()
                self.mostrar_resultados()
            else:
                raise
        except:
            mensagem['fg'] = 'red'
            mensagem['text'] = 'Erro, por favor\n faça o que se pede!!'


jokenpo = Jokenpo()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFC0CB')

titulo = tk.Label(text='Jokenpo', borderwidth=4, relief='raised', bg='#FFB6C1', fg='white',
                  font='Arial 17 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='Pedra, papal ou tesouro?', bg='#FFC0CB', fg='white', font='Arial 12 bold')
aviso.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=jokenpo.escolhas_disponiveis)
escolha.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='', bg='#FFC0CB', fg='white', font='Arial 12 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_jogar = tk.Button(text='Jogar', bg='#FFB6C1', fg='white',
                        font='Arial 14 bold', command=jokenpo.iniciar_jogo)
botao_jogar.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
