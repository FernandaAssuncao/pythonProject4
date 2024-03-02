from datetime import datetime
from tkinter import ttk
import tkinter as tk


class CalculadorDeIdade:
    def __init__(self):
        self.idade = None
        self.ano_atual = None
        self.ano_de_nascimento = None
        self.anos_disponiveis = []
        self.__pegar_ano_atual()
        self.__adicionar_anos()

    def __pegar_ano_atual(self):
        self.ano_atual = datetime.today().year

    def __adicionar_anos(self):
        for c in range(1940, 2060 + 1):
            self.anos_disponiveis.append(c)

    def iniciar_calculadora(self):
       try:
           self.ano_de_nascimento = ano.get()
           self.ano_de_nascimento = int(self.ano_de_nascimento)
           self.idade = self.ano_atual - self.ano_de_nascimento
           aviso['fg'] = 'black'
           aviso['text'] = f'Sua Idade é {self.idade},certo?'
       except:
           aviso['fg'] = 'red'
           aviso['text'] = 'Erro, Algo deu errado'


janela = tk.Tk()
calculadora = CalculadorDeIdade()
janela.title('')
janela.configure(bg='#90EE90')

titulo = tk.Label(text='Calculador de \n Idade', borderwidth=4, relief='raised', bg='#3CB371', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

ano_atual = tk.Label(text=f'Ano Atual: {calculadora.ano_atual}', bg='#2E8B57', fg='black', font='Arial 8 bold')
ano_atual.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Ano de Nascimento', bg='#90EE90', fg='#2E8B57', font='Arial 8 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

ano = ttk.Combobox(values=calculadora.anos_disponiveis)
ano.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#2E8B57', fg='black', font='Arial 8 bold')
aviso.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_calcular_idade = tk.Button(text='Calcular Idade', bg='#3CB371', fg='white', font='Arial 8 bold',
                                 command=calculadora.iniciar_calculadora)
botao_calcular_idade.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
