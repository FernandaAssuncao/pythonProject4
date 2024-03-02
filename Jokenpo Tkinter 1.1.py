from random import choice
from tkinter import ttk
import tkinter as tk


class Jokenpo:
    @staticmethod
    def escolhas_disponiveis():
        lista = ['pedra',
                 'papel',
                 'tesoura']
        return lista

    def __init__(self):
        self.computador = None
        self.usuario = None
        self.pontos_usuarios = 0
        self.pontos_computador = 0
        self.vencedor = ''
        self.escolhas = self.escolhas_disponiveis()

    def escolha_computador(self):
        self.computador = choice(self.escolhas)

    def __marcar_pontos(self):
        if self.vencedor == 'Usuario':
            self.pontos_usuarios += 1
        elif self.vencedor == 'Computador':
            self.pontos_computador += 1

    def atualizar(self):
        self.__marcar_pontos()
        placar['text'] = f'{self.pontos_usuarios} X {self.pontos_computador}'

    def jogar(self):
        try:
            mao = escolha.get()
            mao = str(mao)
            if mao in self.escolhas:
                self.usuario = mao
                self.escolha_computador()
                self.verificar_escolhas()
                self.atualizar()
                aviso['fg'] = 'white'
                aviso['text'] = f'Você escolheu {self.usuario}\nE o computador {self.computador}\nVencedor: {self.vencedor}'
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, algo\n deu errado!'

    def verificar_escolhas(self):
        if (self.usuario == 'pedra') and (self.computador == 'pedra'):
            self.vencedor = 'Empate'
        elif (self.usuario == 'pedra') and (self.computador == 'papel'):
            self.vencedor = 'Computador'
        elif (self.usuario == 'pedra') and (self.computador == 'tesoura'):
            self.vencedor = 'Usuario'
        elif (self.usuario == 'papel') and (self.computador == 'pedra'):
            self.vencedor = 'Usuario'
        elif (self.usuario == 'papel') and (self.computador == 'papel'):
            self.vencedor = 'Empate'
        elif (self.usuario == 'papel') and (self.computador == 'tesoura'):
            self.vencedor = 'Computador'
        elif (self.usuario == 'tesoura') and (self.computador == 'pedra'):
            self.vencedor = 'Computador'
        elif (self.usuario == 'tesoura') and (self.computador == 'papel'):
            self.vencedor = 'Usuario'
        elif (self.usuario == 'tesoura') and (self.computador == 'tesoura'):
            self.vencedor = 'Empate'


jogo = Jokenpo()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFDAB9')

titulo = tk.Label(text='Jokenpo', borderwidth=4, relief='raised', bg='#FFA07A', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

placar = tk.Label(text='0 X 0', bg='#FFDAB9', fg='white', font='Arial 35 bold')
placar.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Pedra, Papel\n ou tesoura?', bg='#FFDAB9', fg='#FF7F50', font='Arial 10 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=jogo.escolhas)
escolha.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFA07A', fg='white', font='Arial 12  bold')
aviso.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_jogar = tk.Button(text='Jo...ken...po', bg='#FFA07A', fg='white', font='Arial 12 bold',
                        command=jogo.jogar)
botao_jogar.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
