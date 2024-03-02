from random import randint
from tkinter import ttk
import tkinter as tk


class ParImpar:
    @staticmethod
    def __gerar_numeros():
        lista = []
        for c in range(1, 11):
            lista.append(c)
        return lista

    def __init__(self):
        self.escolha_usuario = None
        self.escolha_computador = None
        self.numero_usuario = None
        self.numero_computador = None
        self.pontos_computador = 0
        self.pontos_usuario = 0
        self.vencedor = None
        self.soma = None
        self.numeros_disponiveis = self.__gerar_numeros()
        self.escolhas_disponiveis = ['par', 'impar']

    def analisar_escolha(self):
        if self.escolha_usuario == 'par':
            self.escolha_computador = 'impar'
        else:
            self.escolha_computador = 'par'

    def sortear_numero_computador(self):
        self.numero_computador = randint(1, 10)

    def verificar_vencedor(self):
        if self.escolha_usuario == 'par':
            if self.soma % 2 == 0:
                self.vencedor = 'usuario'
            else:
                self.vencedor = 'computador'
        elif self.escolha_usuario == 'impar':
            if self.soma % 2 == 0:
                self.vencedor = 'computador'
            else:
                self.vencedor = 'usuario'

    def somar(self):
        self.soma = self.numero_usuario + self.numero_computador

    def mudar_placar(self):
        placar['text'] = f' {self.pontos_usuario} X {self.pontos_computador} '

    def somar_pontos(self):
        if self.vencedor == 'usuario':
            self.pontos_usuario += 1
        else:
            self.pontos_computador += 1

    def mudar_escolhas(self):
        try:
            escolha_us = escolha.get()
            if escolha_us in self.escolhas_disponiveis:
                self.escolha_usuario = escolha_us
                self.analisar_escolha()
                aviso['fg'] = '#DC143C'
                aviso['text'] = f'Você escolheu {self.escolha_usuario}\nE o computador escolheu {self.escolha_computador}'
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro,escolha não disponivel!!'

    def jogar(self):
        try:
            self.soma = 0
            numero1 = numero.get()
            numero1 = int(numero1)
            if numero1 in self.numeros_disponiveis:
                self.numero_usuario = numero1
                self.sortear_numero_computador()
                self.somar()
                self.verificar_vencedor()
                self.somar_pontos()
                self.mudar_placar()
                aviso1['fg'] = '#DC143C'
                aviso1['text'] = f'Você escolheu {self.numero_usuario}\nE o computador escolheu {self.numero_computador}\nA soma foi {self.soma}\nO vencedor foi {self.vencedor}'
            else:
                raise
        except:
            aviso1['fg'] = 'red'
            aviso1['text'] = 'Erro,algo deu errado!\nprencha tudo que se pede!!'


jogo = ParImpar()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFE4E1')

titulo = tk.Label(text='Jogo do Par \n e Impar', borderwidth=4, relief='ridge', bg='#F08080', fg='#DC143C',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

placar = tk.Label(text=' 0  X  0 ', bg='#FFE4E1', fg='#DC143C', font='Arial 35 bold')
placar.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Escolha entre Par e Impar', bg='#FFE4E1', fg='#DC143C', font='Arial 8 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=jogo.escolhas_disponiveis)
escolha.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFE4E1', fg='#DC143C', font='Arial 8 bold')
aviso.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_escolha = tk.Button(text='Mudar escolha', bg='#F08080', fg='#DC143C', font='Arial 8 bold',
                                command=jogo.mudar_escolhas)
botao_mudar_escolha.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

mensagem1 = tk.Label(text='Escolha um número\n entre 1 e 10', bg='#FFE4E1', fg='#DC143C', font='Arial 8 bold')
mensagem1.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

numero = ttk.Combobox(values=jogo.numeros_disponiveis)
numero.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

aviso1 = tk.Label(text='', bg='#FFE4E1', fg='#DC143C', font='Arial 8 bold')
aviso1.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_numero = tk.Button(text='Jogar', bg='#F08080', fg='#DC143C', font='Arial 8 bold',
                               command=jogo.jogar)
botao_mudar_numero.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar Jogo', bg='#F08080', fg='#DC143C', font='Arial 8 bold',
                         command=janela.quit)
botao_fechar.grid(row=6, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
