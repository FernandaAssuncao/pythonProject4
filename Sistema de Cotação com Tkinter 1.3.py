from tkinter import ttk
import tkinter as tk
import requests


class SistemaCotacao:
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

    def mudar_valor(self):
        for item in self.moedas:
            for chave in item.keys():
                if chave == self.moeda:
                    self.valor = item[chave]

    def resultados_finais(self):
        aviso['fg'] = 'white'
        aviso['text'] = f'A cotação de {self.moeda} é {self.valor}!!'

    def mostrar_cotacao(self):
        try:
            md = escolha.get()
            md = str(md)
            if md in self.moedas_disponiveis:
                self.moeda = md
                self.mudar_valor()
                self.resultados_finais()
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, por favor\n faça o que se pede!!'


sistema = SistemaCotacao()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFC0CB')

titulo = tk.Label(text='Sistema de\n Cotação', bg='#FFB6C1', borderwidth=4, relief='raised', fg='white',
                  font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Escolha aqui a\n moeda desejada', bg='#FFC0CB', fg='white', font='Arial 12 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=sistema.moedas_disponiveis)
escolha.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFB6C1', fg='white', font='Arial 11 bold')
aviso.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_cotacao = tk.Button(text='Mudar Moeda', bg='#FFB6C1', fg='white', font='Arial 13 bold',
                          command=sistema.mostrar_cotacao)
botao_cotacao.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
