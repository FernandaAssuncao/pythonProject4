from tkinter import ttk
import tkinter as tk


class CalculadoraImc:
    @staticmethod
    def __adicionar_altura():
        lista = []
        for c in range(20, 100):
            lista.append(f'1.{c}')
        return lista

    @staticmethod
    def __adicionar_peso():
        lista = []
        for c in range(10, 100):
            for i in range(10, 100):
                lista.append(f'{c}.{i}')
        return lista

    def __init__(self):
        self.peso = None
        self.altura = None
        self.imc = None
        self.faixa = None
        self.alturas_disponiveis = self.__adicionar_altura()
        self.pesos_disponiveis = self.__adicionar_peso()

    def __pegar_valores(self):
        p = pesos.get()
        a = alturas.get()
        a = str(a)
        a = a.replace(',', '.')
        p = str(p)
        p = p.replace(',', '.')
        a = float(a)
        p = float(p)
        self.altura = a
        self.peso = p

    def __calcular_imc(self):
        self.imc = self.peso / (self.altura * self.altura)

    def __verificar_faixas(self):
        if self.imc <= 18.5:
            self.faixa = 'magreza'
        elif (self.imc > 18.5) and (self.imc <= 24.9):
            self.faixa = 'peso normal'
        elif (self.imc >= 25.0) and (self.imc <= 29.9):
            self.faixa = 'sobrepeso'
        elif (self.imc >= 30.0) and (self.imc <= 34.9):
            self.faixa = 'obesidade grau I'
        elif (self.imc >= 35.0) and (self.imc <= 39.9):
            self.faixa = 'obesidade grau II'
        elif self.imc >= 40.0:
            self.faixa = 'obesidade grau III'

    def mostrar_tudo(self):
        self.__calcular_imc()
        self.__verificar_faixas()
        aviso['fg'] = 'white'
        aviso['text'] = f'Imc: {self.imc:.2f}\nFaixa: {self.faixa}'

    def mostrar_imc(self):
        try:
            self.__pegar_valores()
            self.mostrar_tudo()
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, digite\n o que se pede!'


calculadora = CalculadoraImc()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFE4E1')

titulo = tk.Label(text='Calculadora de\n IMC', borderwidth=4, relief='raised', bg='#FFB6C1', fg='white',
                  font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Altura em M', bg='#FFE4E1', fg='#FFB6C1', font='Arial 14 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

alturas = ttk.Combobox(values=calculadora.alturas_disponiveis)
alturas.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem1 = tk.Label(text='Peso com Kg', bg='#FFE4E1', fg='#FFB6C1', font='Arial 14 bold')
mensagem1.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

pesos = ttk.Combobox(values=calculadora.pesos_disponiveis)
pesos.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', borderwidth=4, relief='ridge', bg='#FFC0CB', fg='white',
                 font='Arial 16 bold')
aviso.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_calcular = tk.Button(text='Calcular Imc', bg='#FFB6C1', fg='white', font='Arial 14 bold',
                           command=calculadora.mostrar_imc)
botao_calcular.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
