from random import randint
from tkinter import ttk
import tkinter as tk


class JogoDoDado:
    @staticmethod
    def __adicionar_numeros(num=6):
        lista = []
        for c in range(1, num + 1):
            lista.append(c)
        return lista

    def __init__(self):
        self.dado = None
        self.palpite_usuario = None
        self.palpite_computador = None
        self.vencedor = None
        self.numeros_disponiveis = self.__adicionar_numeros(num=6)

    def girar_dado(self):
        self.dado = randint(1, 6)
        mensagem['fg'] = '#3CB371'
        mensagem['text'] = 'Dado girado com sucesso!'

    def definir_palpite_computador(self):
        self.palpite_computador = randint(1, 6)

    def analisar_vencedor(self):
        if (self.palpite_usuario == self.dado) and (self.palpite_computador == self.dado):
            self.vencedor = 'Empate'
        elif self.palpite_usuario == self.dado:
            self.vencedor = 'Usuario'
        elif self.palpite_computador == self.dado:
            self.vencedor = 'Computador'
        else:
            self.vencedor = 'Nenhum'

    def mostrar_informacoes(self):
        mensagem['fg'] = 'black'
        mensagem['text'] = f'Seu palpite: {self.palpite_usuario}\nPalpite computador: {self.palpite_computador}\nVecedor: {self.vencedor}'

    def inicar_jogo(self):
        try:
            us = usuario.get()
            us = int(us)
            if us in self.numeros_disponiveis and self.dado is not None:
                self.palpite_usuario = us
                self.definir_palpite_computador()
                self.analisar_vencedor()
                self.mostrar_informacoes()
            else:
                raise
        except:
            mensagem['fg'] = 'red'
            mensagem['text'] = 'ERRO, faça\n o que se pede!'


jogo = JogoDoDado()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFEBCD')

titulo = tk.Label(text='Jogo do Dado', borderwidth=4, relief='raised', bg='#FFE4C4',
                  fg='white', font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='Aperte aqui ->\nPara começar', bg='#FFEBCD', fg='white', font='Arial 12 bold')
aviso.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_girar_dado = tk.Button(text='Girar dado', bg='#FFDAB9', fg='white',
                             font='Arial 16 bold', command=jogo.girar_dado)
botao_girar_dado.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

aviso2 = tk.Label(text='Digite seu palpite', bg='#FFEBCD', fg='white', font='Arial 10 bold')
aviso2.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

usuario = ttk.Combobox(values=jogo.numeros_disponiveis)
usuario.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='', bg='#FFEBCD', fg='white', font='Arial 12 bold')
mensagem.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_jogar = tk.Button(text='Tentar', bg='#FFDAB9', fg='white',
                        font='Arial 16 bold', command=jogo.inicar_jogo)
botao_jogar.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
