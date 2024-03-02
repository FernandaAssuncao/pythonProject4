from random import randint
from tkinter import ttk
import tkinter as tk


class SimuladorDeDado:
    def __init__(self):
        self.dado = None
        self.aposta = 1
        self.valor = 0
        self.valores = [c for c in range(1, 7)]

    def girar_dado(self):
        self.dado = randint(1, 6)
        dado['text'] = f'Dado: {self.dado}'
        self.aumentar_valor()

    def aumentar_valor(self):
        if self.dado == self.aposta:
            self.valor += 1
        self.__mudar_texto()

    def __mudar_texto(self):
        valorr['text'] = f'{self.aposta}: {self.valor}'

    def mudar_valor_aposta(self):
       try:
           aposta = apostaa.get()
           aposta = int(aposta)
           if aposta in self.valores:
               self.aposta = aposta
               self.valor = 0
               valorr['fg'] = 'black'
               valorr['text'] = f'{self.aposta}: {self.valor}'
           else:
               raise
       except:
           valorr['fg'] = 'red'
           valorr['text'] = 'Erro,algo deu errado'


simulador = SimuladorDeDado()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFE4E1')

titulo = tk.Label(text='Simulador de\n Dado', borderwidth=4, relief='raised', bg='#FFB6C1', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

dado = tk.Label(text='', bg='#FFE4E1', fg='black', font='Arial 8 bold')
dado.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_dado = tk.Button(text='Girar Dado', bg='#FFC0CB', fg='white', font='Arial 12 bold',
                       command=simulador.girar_dado)
botao_dado.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Aposta', borderwidth=4, relief='raised', bg='#FFB6C1',
                   fg='white', font='Arial 12 bold')
titulo2.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Aposte que número\n q vai cair no Dado', bg='#FFE4E1', fg='black', font='Arial 8 bold')
mensagem.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

apostaa = ttk.Combobox(values=simulador.valores)
apostaa.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

valorr = tk.Label(text='', borderwidth=4, relief='ridge', bg='#FFE4E1', fg='black', font='Arial 8 bold')
valorr.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_aposta = tk.Button(text='Apostar', bg='#FFC0CB', fg='white', font='Arial 12 bold',
                               command=simulador.mudar_valor_aposta)
botao_mudar_aposta.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
