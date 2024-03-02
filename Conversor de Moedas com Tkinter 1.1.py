from tkinter import ttk
import tkinter as tk
import requests


class SistemaDeConversorDeMoedas:
    @staticmethod
    def __mudar_valores():
        lista = []
        for c in range(1, 1001):
            lista.append(c)
        return lista

    def __init__(self):
        self.moeda_escolhida = None
        self.valor_moeda = None
        self.usuario = None
        self.resultado = None
        self.moedas = []
        self.moedas_disponiveis = []
        self.valores_disponiveis = self.__mudar_valores()
        self.__pegar_moeda()

    def __pegar_valor(self):
        for m, i in self.moedas:
            if self.moeda_escolhida == m:
                self.valor_moeda = float(i)

    def __pegar_moeda(self):
        link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
        requisicao = requests.get(link)
        dic = requisicao.json()
        for item in dic.keys():
            self.moedas_disponiveis.append(item)
            self.moedas.append((item, float(dic[item]['bid'])))

    def mudar_escolha(self):
        try:
            md = escolha.get()
            md = str(md)
            if md in self.moedas_disponiveis:
                self.moeda_escolhida = md
                self.__pegar_valor()
                aviso['fg'] = 'black'
                aviso['text'] = f'Moeda alterada para\n {self.moeda_escolhida} com sucesso!'
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, algo\n deu errado!'

    def calcular_valor(self):
        self.resultado = self.valor_moeda * self.usuario

    def mostrar_resultado(self):
        aviso1['fg'] = 'black'
        aviso1['text'] = f'{self.usuario} = R${self.resultado:.2f}'

    def mostrar_valor(self):
        try:
            valor = valorr.get()
            valor = float(valor)
            self.usuario = valor
            self.calcular_valor()
            self.mostrar_resultado()
        except:
            aviso1['fg'] = 'red'
            aviso1['text'] = 'Erro, digite um\n valor valido!'


conversor = SistemaDeConversorDeMoedas()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFEBCD')

titulo = tk.Label(text='Conversor de\n Moedas', borderwidth=4, relief='ridge', bg='#FFDAB9', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Escolha uma\n moeda aqui', bg='#FFEBCD', fg='white', font='Arial 12 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=conversor.moedas_disponiveis)
escolha.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFEBCD', fg='white', font='Arial 10 bold')
aviso.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_moeda = tk.Button(text='Mudar Moeda', bg='#FFDAB9', fg='white', font='Arial 12 bold',
                              command=conversor.mudar_escolha)
botao_mudar_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Converter moeda\n pra valor desejado', borderwidth=4, relief='ridge', bg='#FFDAB9',
                   fg='white', font='Arial 15 bold')
titulo2.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem1 = tk.Label(text='Digite aqui\n um valor', bg='#FFEBCD', fg='white', font='Arial 12 bold')
mensagem1.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

valorr = ttk.Combobox(values=conversor.valores_disponiveis)
valorr.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

aviso1 = tk.Label(text='', bg='#FFEBCD', fg='white', font='Arial 10 bold')
aviso1.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mostrar_valor = tk.Button(text='Moeda pra Real', bg='#FFDAB9', fg='white', font='Arial 12 bold',
                                command=conversor.mostrar_valor)
botao_mostrar_valor.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
