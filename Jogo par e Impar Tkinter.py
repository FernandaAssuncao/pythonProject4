from tkinter import ttk
from random import randint
import tkinter as tk


class JogoParImpar:
    def __init__(self):
        self.soma = None
        self.escolha_usuario = None
        self.escolha_computador = None
        self.escolha_numero_usuario = None
        self.escolha_numero_computador = None
        self.lista_opcoes = ['par',
                             'impar']
        self.numeros = [c for c in range(1, 11)]

    def mudar_escolhas(self):
        try:
            escolha_usuario = escolha.get()
            escolha_usuario = str(escolha_usuario)
            if escolha_usuario in self.lista_opcoes:
                self.escolha_usuario = escolha_usuario
                if self.escolha_usuario == 'par':
                    self.escolha_computador = 'impar'
                else:
                    self.escolha_computador = 'par'
                aviso1['fg'] = '#4B0082'
                aviso1['text'] = f'Você escolheu {self.escolha_usuario}\ne o computador ficou com {self.escolha_computador}'
            else:
                raise
        except:
            aviso1['fg'] = 'red'
            aviso1['text'] = 'Opção invalida'

    def mudar_numero(self):
        try:
            numero = escolha_numero.get()
            numero = int(numero)
            if numero in self.numeros:
                self.escolha_numero_usuario = numero
                self.escolha_numero_computador = randint(1, 10)
                aviso2['fg'] = '#4B0082'
                aviso2['text'] = f'Você escolheu o número {self.escolha_numero_usuario}\nE o computador escolheu o número {self.escolha_numero_computador}'
            else:
                raise
        except:
            aviso2['fg'] = 'red'
            aviso2['text'] = 'Erro,digite um número VALÍDO'

    def __somar(self):
        self.soma = self.escolha_numero_usuario + self.escolha_numero_computador

    def veficar_vencedor(self):
        try:
            self.__somar()
            if self.escolha_usuario == 'par':
                if self.soma % 2 == 0:
                    vencedor['fg'] = '#4B0082'
                    vencedor['text'] = f'A soma dos dois números deu {self.soma}\nParabens você venceu'
                else:
                    vencedor['fg'] = '#4B0082'
                    vencedor['text'] = f'A soma dos dois números deu {self.soma}\nO computador venceu'
            elif self.escolha_usuario == 'impar':
                if self.soma % 2 == 0:
                    vencedor['fg'] = '#4B0082'
                    vencedor['text'] = f'A soma dos dois números deu {self.soma}\nO computador venceu'
                else:
                    vencedor['fg'] = '#4B0082'
                    vencedor['text'] = f'A soma dos dois números deu {self.soma}\nParabens você venceu'
        except:
            vencedor['fg'] = 'red'
            vencedor['text'] = 'Erro,preencha todos os campos\nacima para jogar!'


janela = tk.Tk()
jogo = JogoParImpar()
janela.configure(background='#9370DB')
janela.title('Par e Impar')

titulo = tk.Label(text='Jogo do Par e Impar', relief='ridge', borderwidth=4, bg='#8A2BE2', fg='black')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Escolha aqui entre Par e Impar', bg='#9370DB', fg='#4B0082')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=jogo.lista_opcoes)
escolha.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

aviso1 = tk.Label(text='', bg='#9370DB', fg='#4B0082')
aviso1.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_escolha = tk.Button(text='Mudar escolha', bg='#A020F0', fg='#4B0082', command=jogo.mudar_escolhas)
botao_mudar_escolha.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

titulo1 = tk.Label(text='Mudar Número', relief='ridge', borderwidth=4, bg='#8A2BE2', fg='black')
titulo1.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem2 = tk.Label(text='Escola aqui um número entre 1 e 10', bg='#9370DB', fg='#4B0082')
mensagem2.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha_numero = ttk.Combobox(values=jogo.numeros)
escolha_numero.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

aviso2 = tk.Label(text='', bg='#9370DB', fg='#4B0082')
aviso2.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_escolha_numero = tk.Button(text='Mudar Número', bg='#A020F0', fg='#4B0082', command=jogo.mudar_numero)
botao_escolha_numero.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

vencedor = tk.Label(text='', bg='#9370DB', fg='#4B0082')
vencedor.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_jogar = tk.Button(text='Jogar', bg='#A020F0', fg='#4B0082', command=jogo.veficar_vencedor)
botao_jogar.grid(row=6, column=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar', bg='#A020F0', fg='#4B0082', command=janela.quit)
botao_fechar.grid(row=7, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
