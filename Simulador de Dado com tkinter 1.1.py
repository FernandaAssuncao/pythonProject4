from random import randint
from tkinter import ttk
import tkinter as tk


class SimuladorDeDado:
    @staticmethod
    def adicionar_valores():
        lista = []
        for c in range(1, 7):
            lista.append(c)
        return lista

    def __init__(self):
        self.dado = 0
        self.chute_usuario = 0
        self.quant_usuario = 0
        self.chute_computador = 0
        self.quant_computador = 0
        self.valores_disponiveis = self.adicionar_valores()

    def girar_dado(self):
        self.dado = randint(1, 6)
        dd['text'] = f'Caiu {self.dado}!'
        if self.chute_usuario != 0:
            if self.dado == self.chute_usuario:
                self.quant_usuario += 1
                aviso['text'] = f'Seu chute {self.chute_usuario}: {self.quant_usuario}'
            elif self.dado == self.chute_computador:
                self.quant_computador += 1
                aviso2['text'] = f'Chute do computador: {self.chute_computador}: {self.quant_computador}'


    def mudar_valor_aposta_computador(self):
        self.chute_computador = randint(1, 6)
        aviso2['text'] = f'Chute de computador: {self.chute_computador}: 0'

    def mudar_valor_aposta(self):
        try:
            valor = usuario.get()
            valor = int(valor)
            if valor in self.valores_disponiveis:
                self.quant_usuario = 0
                self.quant_computador = 0
                self.chute_usuario = valor
                aviso['fg'] = '#FFDAB9'
                aviso['text'] = f'Seu chute: {self.chute_usuario}: '
                self.mudar_valor_aposta_computador()
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro,digite\n o que se pede!'


simulador = SimuladorDeDado()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFEFD5')

titulo = tk.Label(text='Simulador de\n Dado', borderwidth=4, relief='raised', bg='#FFDAB9', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

dd = tk.Label(text='', bg='white', fg='#FFDAB9', font='Arial 10 bold')
dd.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_girar_dado = tk.Button(text='Girar Dado', bg='#FFDAB9', fg='white', font='Arial 12 bold',
                             command=simulador.girar_dado)
botao_girar_dado.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Sessão de\n Apostas', borderwidth=4, relief='raised', bg='#FFDAB9', fg='white',
                   font='Arial 15 bold')
titulo2.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Aposte aqui\n um número', bg='white', fg='#FFDAB9', font='Arial 10 bold')
mensagem.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

usuario = ttk.Combobox(values=simulador.valores_disponiveis)
usuario.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='white', fg='#FFDAB9', font='Arial 10 bold')
aviso.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_apostar = tk.Button(text='Apostar', bg='#FFDAB9', fg='white', font='Arial 12 bold',
                          command=simulador.mudar_valor_aposta)
botao_apostar.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

aviso2 = tk.Label(text='', bg='white', fg='#FFDAB9', font='Arial 10 bold')
aviso2.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
