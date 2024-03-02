from tkinter import ttk
import tkinter as tk


class CalculadoraDeDescontos:
    @staticmethod
    def __adicionar_valores():
        lista = []
        for c in range(1, 1001):
            lista.append(c)
        return lista

    @staticmethod
    def __adicionar_descontos():
        lista = []
        for c in range(1, 101):
            lista.append(c)
        return lista

    def __init__(self):
        self.porcentagem = None
        self.valor = None
        self.valor_desconto = None
        self.desconto_disponiveis = self.__adicionar_descontos()
        self.valores_disponiveis = self.__adicionar_valores()

    def tratar_valor(self, valor):
        valor = str(valor)
        valor = valor.replace(',', '.')
        valor = float(valor)
        self.valor = valor

    def calcular_desconto(self):
        self.valor_desconto = self.valor * self.porcentagem / 100

    def mudar_e_mostrar_resultados(self):
        try:
            descont = valor_desconto.get()
            descont = int(descont)
            valorr = valor_escolhido.get()
            self.tratar_valor(valor=valorr)
            self.porcentagem = descont
            self.calcular_desconto()
            mostrar['fg'] = '#FFB6C1'
            mostrar['text'] = f'{self.porcentagem}% de R${self.valor} = R${self.valor_desconto}'
        except:
            mostrar['fg'] = 'red'
            mostrar['text'] = 'Erro, por favor\n faça tudo que se pede!'


calculadora = CalculadoraDeDescontos()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFE4E1')

titulo = tk.Label(text='Calculador de\n Descontos', borderwidth=4, relief='raised', bg='#FFB6C1',
                  fg='white', font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky=' nswe')

mensagem1 = tk.Label(text='Valor do desconto?', bg='#FFE4E1', fg='#FFB6C1', font='Arial 10 bold')
mensagem1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

valor_desconto = ttk.Combobox(values=calculadora.desconto_disponiveis)
valor_desconto.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem2 = tk.Label(text='Valor que\n você deseja?', bg='#FFE4E1', fg='#FFB6C1', font='Arial 10 bold')
mensagem2.grid(row=2, column=0, columnspan=2, padx=10, sticky='nswe')

valor_escolhido = ttk.Combobox(values=calculadora.valores_disponiveis)
valor_escolhido.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

mostrar = tk.Label(text='', bg='#FFE4E1', fg='#FFB6C1', font='Arial 12 bold')
mostrar.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mostrar = tk.Button(text='Calcular Desconto', bg='#FFB6C1', fg='white', font='Arial 15 bold',
                          command=calculadora.mudar_e_mostrar_resultados)
botao_mostrar.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
