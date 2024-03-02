from tkinter import ttk
import tkinter as tk
import requests


class SistemaDeCotacao:
    def __init__(self):
        self.moeda = None
        self.valor = None
        self.moedas = []
        self.moedas_disponiveis = []
        self.__adicionar_moedas()
        self.mudar_valor()

    def __adicionar_moedas(self):
        link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
        requisicao = requests.get(link)
        dic = requisicao.json()
        for item in dic.keys():
            self.moedas_disponiveis.append(item)
            self.moedas.append({item: float(dic[item]['bid'])})

    def mudar_valor(self):
        for item in self.moedas:
            for chave in item.keys():
                if chave == self.moeda:
                    self.valor = item[chave]

    def mostrar_cotacao(self):
        try:
            md = escolha.get()
            md = str(md)
            if md in self.moedas_disponiveis:
                self.moeda = md
                self.mudar_valor()
                mostrar['fg'] = 'white'
                mostrar['text'] = f'A cotação de\n {self.moeda} é {self.valor}'
            else:
                raise
        except:
            mostrar['fg'] = 'red'
            mostrar['text'] = 'Erro, por favor\n faça o que se pede!'


sistema = SistemaDeCotacao()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFE4C4')

titulo = tk.Label(text='Sistema de\n Cotação', borderwidth=4, relief='raised', bg='#FFDAB9',
                  fg='white', font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Escolha uma Moeda', bg='#FFE4C4', fg='white', font='Arial 12 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=sistema.moedas_disponiveis)
escolha.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mostrar = tk.Label(text='', borderwidth=4, relief='ridge', bg='#FFDAB9',
                   fg='white', font='Arial 14 bold')
mostrar.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mostrar = tk.Button(text='Mudar Moeda', bg='#FFDAB9', fg='white', font='Arial 12 bold',
                          command=sistema.mostrar_cotacao)
botao_mostrar.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
