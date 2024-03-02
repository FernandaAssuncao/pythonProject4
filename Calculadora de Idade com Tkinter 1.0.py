from datetime import datetime
from tkinter import ttk
import tkinter as tk


class CalculadoraDeIdade:
    @staticmethod
    def adicionar_anos():
        lista = []
        for c in range(1920, 2051):
            lista.append(c)
        return lista

    @staticmethod
    def pegar_ano_atual():
        anoo = datetime.today().year
        return anoo

    def __init__(self):
        self.ano_de_nasciemento = None
        self.ano_atual = None
        self.idade = None
        self.anos_disponiveis = self.adicionar_anos()
        self.mudar_ano_atual()

    def mudar_ano_atual(self):
        self.ano_atual = self.pegar_ano_atual()

    def mostrar_idade(self):
        aviso['fg'] = 'white'
        aviso['text'] = f'Você tem {self.idade}\n anos, certo?'

    def calcular_idade(self):
        try:
            anoo = ano.get()
            anoo = int(anoo)
            self.ano_de_nasciemento = anoo
            self.idade = self.ano_atual - self.ano_de_nasciemento
            self.mostrar_idade()
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, por favor\n digie o que se pede!'


calculadora = CalculadoraDeIdade()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#E0FFFF')

titulo = tk.Label(text='Calculadora de\n Idade', borderwidth=4, relief='raised', bg='#B0E0E6', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

ano_atual = tk.Label(text=f'Ano Atual: {calculadora.ano_atual}', borderwidth=4, relief='ridge', bg='#B0E0E6',
                     fg='white', font='Arial 12 bold')
ano_atual.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='  Ano de \n Nascimento  ', bg='#E0FFFF', fg='#B0E0E6', font='Arial 10 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

ano = ttk.Combobox(values=calculadora.anos_disponiveis)
ano.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#B0E0E6', fg='white', font='Arial 12 bold')
aviso.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_calcular_valor = tk.Button(text='Calcular Idade', bg='#B0E0E6', fg='white', font='Arial 13 bold',
                                 command=calculadora.calcular_idade)
botao_calcular_valor.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
