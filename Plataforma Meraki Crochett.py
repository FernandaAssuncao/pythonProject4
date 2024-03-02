from tkinter import ttk
import tkinter as tk


class CalculadoraDePrecos:
    @staticmethod
    def lista_precos():
        lista = []
        for c in range(1, 80):
            texto = f'{c}.00'
            valor = float(texto)
            lista.append(valor)
        return lista

    @staticmethod
    def lista_quantidade():
        lista = []
        for c in range(1, 101):
            lista.append(c)
        return lista

    def __init__(self):
        self.preco_pecas = 0.0
        self.quantidade_pecas = 0
        self.valor = 0.0
        self.precos_disponiveis = self.lista_precos()
        self.quantidade_disponiveis = self.lista_quantidade()

    def calculadora(self):
        try:
            valor = preco.get()
            quantidade = quant.get()
            valor = float(valor)
            quantidade = int(quantidade)
            self.valor = valor * quantidade
            resultado['fg'] = 'white'
            resultado['text'] = f'Resultado: R${self.valor:.2f}'
        except:
            resultado['fg'] = 'red'
            resultado['text'] = 'Erro, faça o que se pede!'



calculadora = CalculadoraDePrecos()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFB6C1')

titulo = tk.Label(text='Calculador de\n Preços', borderwidth=4, relief='ridge', bg='#FFC0CB', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Valor da Peça', bg='#FFB6C1', fg='white', font='Arial 10 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

preco = ttk.Combobox(values=calculadora.precos_disponiveis)
preco.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem1 = tk.Label(text='Quantidade de Peças', bg='#FFB6C1', fg='white', font='Arial 10 bold')
mensagem1.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

quant = ttk.Combobox(values=calculadora.quantidade_disponiveis)
quant.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

resultado = tk.Label(text='', bg='#FFB6C1', fg='white', font='Arial 10 bold')
resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_calculadora = tk.Button(text='Calcular Preço', bg='#FFC0CB', fg='white', font='Arial 12 bold',
                              command=calculadora.calculadora)
botao_calculadora.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
