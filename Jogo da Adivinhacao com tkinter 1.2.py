from random import randint
from tkinter import ttk
import tkinter as tk


class JogoDaAdivinhacao:
    @staticmethod
    def adicionar_numeros():
        lista = []
        for c in range(1, 51):
            lista.append(c)
        return lista

    def __init__(self):
        self.usuario = None
        self.tentativas = 10
        self.numero_sorteado = None
        self.numeros_disponiveis = self.adicionar_numeros()

    def reiniciar_tentativas(self):
        self.tentativas = 10
        mensagem_tentativa['text'] = f'Tentativas: {self.tentativas}'

    def sortear_valor(self):
        self.reiniciar_tentativas()
        self.numero_sorteado = randint(1, 50)

    def verificar_tentativas(self):
        if self.usuario == self.numero_sorteado:
            aviso['fg'] = 'white'
            aviso['text'] = f'Parabens você acertou!\nO número sorteado foi {self.numero_sorteado}\nJOGO REINICIADO'
            self.sortear_valor()
        elif self.tentativas == 0 or self.tentativas < 0:
            aviso['fg'] = 'white'
            aviso['text'] = 'Suas tentativas acabaram!\nSortei novamente para reiniciar!'
        else:
            if self.usuario > self.numero_sorteado:
                aviso['fg'] = 'white'
                aviso['text'] = f'Você errou!\nValor muito alto'
            else:
                aviso['fg'] = 'white'
                aviso['text'] = f'Você errou!\nValor muito baixo!'

    def diminuir_tentativas(self):
        if self.tentativas < 0:
            self.tentativas = 0
        else:
            self.tentativas -= 1
        self.mostrar_tentativas()

    def mostrar_tentativas(self):
        mensagem_tentativa['text'] = f'Tentativas: {self.tentativas}'

    def jogar(self):
        try:
            nume = num.get()
            nume = int(nume)
            if nume in self.numeros_disponiveis:
                self.usuario = nume
                self.diminuir_tentativas()
                self.verificar_tentativas()
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, faça\n o que se pede!'


jogo = JogoDaAdivinhacao()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#E0FFFF')

titulo = tk.Label(text='Jogo da\n Adivinhacao', borderwidth=4, relief='raised', bg='#B0E0E6', fg='white',
                  font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem_tentativa = tk.Label(text='Tentativas: ', bg='#B0E0E6', fg='white', font='Arial 12 bold')
mensagem_tentativa.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_sortear_valor = tk.Button(text='Sortear Numero', bg='#B0E0E6', fg='white', font='Arial 14 bold',
                                command=jogo.sortear_valor)
botao_sortear_valor.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Chute um número\n entre 1 e 50', bg='#E0FFFF', fg='#B0E0E6', font='Arial 10 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

num = ttk.Combobox(values=jogo.numeros_disponiveis)
num.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#B0E0E6', fg='white', font='Arial 12 bold')
aviso.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_jogar = tk.Button(text='Jogar', bg='#B0E0E6', fg='white', font='Arial 14 bold',
                        command=jogo.jogar)
botao_jogar.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
