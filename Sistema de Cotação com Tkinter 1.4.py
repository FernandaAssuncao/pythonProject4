from tkinter import ttk
import tkinter as tk
import requests


class Cotacao:
    def __init__(self):
        self.moeda = None
        self.valor = None
        self.moedas = []
        self.moedas_disponiveis = []
        self.__adicionar_moedas()

    def __adicionar_moedas(self):
        link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
        requisicao = requests.get(link)
        dic = requisicao.json()
        for item in dic.keys():
            self.moedas_disponiveis.append(item)
            self.moedas.append({item: float(dic[item]['bid'])})

    def __mudar_valor(self):
        for item in self.moedas:
            for chave in item.keys():
                if chave == self.moeda:
                    self.valor = item[chave]

    def __mudar_mensagem(self):
        mensagem['fg'] = 'white'
        mensagem['text'] = f'A cotação da moeda {self.moeda}\n é {self.valor}'

    def iniciar_sistema(self):
        try:
            md = moeda_escolhida.get()
            md = str(md)
            if md in self.moedas_disponiveis:
                self.moeda = md
                self.__mudar_valor()
                self.__mudar_mensagem()
            else:
                raise
        except:
            mensagem['fg'] = 'red'
            mensagem['text'] = 'Erro, por favor\n faça o que se pede!!'


sistema = Cotacao()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFE4C4')

titulo = tk.Label(text='Sistema de Cotação', borderwidth=4, relief='raised', bg='#FFDAB9',
                  fg='white', font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='Escolha uma moeda aqui,\n para saber sua cotação', bg='#FFE4C4', fg='white',
                 font='Arial 13 bold')
aviso.grid(row=1, column=0, columnspan=2, padx=10, sticky='nswe')

moeda_escolhida = ttk.Combobox(values=sistema.moedas_disponiveis)
moeda_escolhida.grid(row=1, column=2, padx=10, sticky='nswe')

mensagem = tk.Label(text='', bg='#FFDAB9', fg='white', font='Arial 12 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_cotacao = tk.Button(text='Ver Cotação', bg='#FFDAB9', fg='white',
                          font='Arial 16 bold', command=sistema.iniciar_sistema)
botao_cotacao.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
