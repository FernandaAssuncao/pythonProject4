from tkinter import ttk
import tkinter as tk
import requests


class SistemaDeCotacao:
    def __init__(self):
        self.moeda_escolhida = None
        self.valor = None
        self.moedas_disponiveis = []
        self.moedas = []
        self.__pegar_moeda()

    def __pegar_moeda(self):
        link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
        requisicao = requests.get(link)
        dic = requisicao.json()
        for item in dic.keys():
            self.moedas_disponiveis.append(item)
            self.moedas.append((item, float(dic[item]['bid'])))

    def mostrar_cotacao(self):
        try:
            moedaa = moeda.get()
            moedaa = str(moedaa)
            if moedaa in self.moedas_disponiveis:
                self.moeda_escolhida = moedaa
                self.__mostrar_valor()
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, faça\n o que se pede!'

    def __mostrar_valor(self):
        for item, valor in self.moedas:
            if self.moeda_escolhida == item:
                aviso['fg'] = 'white'
                aviso['text'] = f'A cotação do {self.moeda_escolhida}\n é {valor:.2f}'


sistema = SistemaDeCotacao()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#90EE90')

titulo = tk.Label(text='Conversor de\n Moedas', borderwidth=4, relief='raised', bg='#3CB371', fg='white',
                  font='Arial 19 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Escolha uma\n moeda aqui!', bg='#90EE90', fg='#3CB371', font='Arial 12 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

moeda = ttk.Combobox(values=sistema.moedas_disponiveis)
moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#90EE90', fg='white', font='Arial 10 bold')
aviso.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_cotacao = tk.Button(text='Ver cotação', bg='#3CB371', fg='white', font='Arial 12 bold',
                          command=sistema.mostrar_cotacao)
botao_cotacao.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
