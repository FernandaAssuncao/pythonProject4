from random import choice
from tkinter import ttk
import tkinter as tk


class Jokenpo:
    def __init__(self):
        self.usuario = None
        self.computador = None
        self.vencedor = None
        self.pontos_usuario = 0
        self.pontos_computador = 0
        self.escolhas_disponiveis = ['pedra',
                                     'papel',
                                     'tesoura']

    def mudar_escolha_computador(self):
        self.computador = choice(self.escolhas_disponiveis)

    def mostrar_escolhas(self):
        escolha1['text'] = f'{self.usuario}'
        escolha2['text'] = f'{self.computador}'

    def verificar_escolhas(self):
        if (self.usuario == 'pedra') and (self.computador == 'pedra'):
            self.vencedor = 'empate'
        elif (self.usuario == 'pedra') and (self.computador == 'papel'):
            self.vencedor = 'computador'
        elif (self.usuario == 'pedra') and (self.computador == 'tesoura'):
            self.vencedor = 'usuario'
        elif (self.usuario == 'papel') and (self.computador == 'pedra'):
            self.vencedor = 'usuario'
        elif (self.usuario == 'papel') and (self.computador == 'papel'):
            self.vencedor = 'empate'
        elif (self.usuario == 'papel') and (self.computador == 'tesoura'):
            self.vencedor = 'computador'
        elif (self.usuario == 'tesoura') and (self.computador == 'pedra'):
            self.vencedor = 'computador'
        elif (self.usuario == 'tesoura') and (self.computador == 'papel'):
            self.vencedor = 'usuario'
        elif (self.usuario == 'tesoura') and (self.computador == 'tesoura'):
            self.vencedor = 'empate'

    def mostrar_vencedor(self):
        self.verificar_escolhas()
        vitoria['text'] = f'Vencedor: {self.vencedor}'

    def calcular_pontos(self):
        if self.vencedor == 'usuario':
            self.pontos_usuario += 1
        elif self.vencedor == 'computador':
            self.pontos_computador += 1
        else:
            pass

    def atualizar_pontos(self):
        self.calcular_pontos()
        placar['text'] = f'{self.pontos_usuario}  X {self.pontos_computador}'

    def jogar(self):
        try:
            e = escolha.get()
            e = str(e)
            if e in self.escolhas_disponiveis:
                self.usuario = e
                self.mudar_escolha_computador()
                self.mostrar_escolhas()
                self.mostrar_vencedor()
                self.atualizar_pontos()
            else:
                raise
        except:
            mensagem2['fg'] = 'red'
            mensagem2['text'] = 'Erro, digite\n o que se pede!'


jogo = Jokenpo()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#90EE90')

titulo = tk.Label(text='Jokenpo', borderwidth=4, relief='raised', bg='#3CB371', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

placar = tk.Label(text='0 X 0', bg='#90EE90', fg='white', font='Arial 25 bold')
placar.grid(row=1, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Pedra, Papel\n ou tesoura?', bg='#90EE90', fg='#3CB371', font='Arial 10 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=jogo.escolhas_disponiveis)
escolha.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

mensagem2 = tk.Label(text='', bg='#3CB371', fg='white', font='Arial 12 bold')
mensagem2.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_jogar = tk.Button(text='Jogar', bg='#3CB371', fg='white', font='Arial 12 bold',
                        command=jogo.jogar)
botao_jogar.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

escolha1 = tk.Label(text='Sua escolha: ', borderwidth=4, relief='ridge', bg='#3CB371', fg='white',
                    font='Arial 12 bold')
escolha1.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha2 = tk.Label(text='Escolha computador: ', borderwidth=4, relief='ridge', bg='#3CB371',
                    fg='white', font='Arial 12 bold')
escolha2.grid(row=4, column=2, columnspan=1, padx=10, pady=10, sticky='nswe')

vitoria = tk.Label(text='Vencedor: ', borderwidth=4, relief='raised', bg='#3CB371',
                   fg='white', font='Arial 14 bold')
vitoria.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar Jogo', bg='#3CB371', fg='white', font='Arial 12 bold',
                         command=janela.quit)
botao_fechar.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
