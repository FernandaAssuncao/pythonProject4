from tkinter import ttk
import tkinter as tk


class CalculadoraDeImc:
    @staticmethod
    def __alturas_disponiveis():
        lista = []
        for c in range(0, 100):
            lista.append('1.' + str(c))
        return lista

    @staticmethod
    def __pesos_disponiveis():
        lista = []
        for c in range(10, 150):
            for i in range(0, 100):
                lista.append(f'{str(c)}.' + f'{str(i)}')
        return lista

    def __init__(self):
        self.altura = None
        self.peso = None
        self.imc = None
        self.faixa = None
        self.alturas = self.__alturas_disponiveis()
        self.pesos = self.__pesos_disponiveis()

    def calcular(self):
        try:
            pesos = peso.get()
            alturass = altura.get()
            self.peso = float(pesos)
            self.altura = float(alturass)
            self.imc = self.peso / (self.altura * self.altura)
            self.faixas_imc()
            mensagem_imc['fg'] = '#FF4500'
            mensagem_imc['text'] = f'Seu imc é {self.imc:.2f}\nFaixa: {self.faixa}'
        except:
            mensagem_imc['fg'] = 'red'
            mensagem_imc['text'] = 'Algo deu errado!'

    def faixas_imc(self):
        if self.imc is not None:
            if self.imc <= 18.5:
                self.faixa = 'Abaixo do Peso'
            elif (self.imc >= 18.6) and (self.imc <= 24.9):
                self.faixa = 'Peso Normal'
            elif (self.imc >= 25.0) and (self.imc <= 29.0):
                self.faixa = 'Sobrepeso'
            elif (self.imc >= 30.0) and (self.imc <= 34.9):
                self.faixa = 'Obesidade grau I'
            elif (self.imc >= 35.0) and (self.imc <= 39.9):
                self.faixa = 'Obesidade grau II'
            elif self.imc > 40.0:
                self.faixa = 'Obesidade grau III'


janela = tk.Tk()
calculadora = CalculadoraDeImc()
janela.title('')
janela.configure(bg='#FFE4C4')

titulo = tk.Label(text='Calculador de \nIMC', borderwidth=4, relief='ridge', bg='#FF7F50', fg='white',
                  font='Arial 16 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Altura em M', bg='#FFE4C4', fg='#FF4500', font='Arial 12 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

altura = ttk.Combobox(values=calculadora.alturas)
altura.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem2 = tk.Label(text='Peso em Kg', bg='#FFE4C4', fg='#FF4500', font='Arial 12 bold')
mensagem2.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

peso = ttk.Combobox(values=calculadora.pesos)
peso.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

mensagem_imc = tk.Label(text='', bg='#FFA07A', fg='#FF4500', font='Arial 8 bold')
mensagem_imc.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_calcular_imc = tk.Button(text='Calcular Imc', bg='#FF4500', fg='black', font='Arial 10 bold',
                               command=calculadora.calcular)
botao_calcular_imc.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar Calculadora', bg='#FF4500', fg='black', font='Arial 10 bold',
                         command=janela.quit)
botao_fechar.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
