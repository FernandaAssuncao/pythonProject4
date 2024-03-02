from tkinter import ttk
import tkinter as tk
import requests


class SistemaDeCotacao:
    def __init__(self):
        self.moeda = None
        self.valor = None
        self.moedas = []
        self.moedas_disponiveis = []
        self.__adicionar_moedas_a_listas()

    def __adicionar_moedas_a_listas(self):
        link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
        requisicao = requests.get(link)
        dic = requisicao.json()
        for item in dic.keys():
            self.moedas.append((item, dic[item]['bid']))
            self.moedas_disponiveis.append(item)

    def __pegar_moeda(self):
        for item, valor in self.moedas:
            if item == self.moeda:
                self.valor = valor
        mostrar['fg'] = 'white'
        mostrar['text'] = f'O valor do {self.moeda}\n é {self.valor}'

    def sistema_cotacao(self):
        try:
            m = escolha.get()
            m = str(m)
            if m in self.moedas_disponiveis:
                self.moeda = m
                self.__pegar_moeda()
            else:
                raise
        except:
            mostrar['fg'] = 'red'
            mostrar['text'] = 'Erro, faça\n o que se pede!'


sistema = SistemaDeCotacao()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFE4E1')

titulo = tk.Label(text='Sistema de\n Cotações', borderwidth=4, relief='raised', bg='#FFC0CB', fg='white',
                  font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Escola aqui\n uma\n moeda', bg='#FFE4E1', fg='#FFC0CB', font='Arial 12 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=sistema.moedas_disponiveis)
escolha.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mostrar = tk.Label(text='', bg='#FFB6C1', fg='white', font='Arial 10 bold')
mostrar.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mostrar_cotacao = tk.Button(text='Mostrar valor moeda', bg='#FFC0CB', fg='white',
                                  font='Arial 15 bold', command=sistema.sistema_cotacao)
botao_mostrar_cotacao.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
