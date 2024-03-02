from tkinter import ttk
import tkinter as tk
import requests


class ConversorDeMoedas:
    def __init__(self):
        self.moeda_escolhida = None
        self.valor_moeda = None
        self.usuario_real = None
        self.moedas_disponiveis = []
        self.moedas = []
        self.__pegar_moedas()

    def __pegar_moedas(self):
        link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
        requisicao = requests.get(link)
        dic = requisicao.json()
        for item in dic:
            self.moedas_disponiveis.append(item)
            self.moedas.append((item, dic[item]['bid']))

    def mudar_moeda(self):
        try:
            escolhida = moeda.get()
            if escolhida in self.moedas_disponiveis:
                self.moeda_escolhida = escolhida
                self.mudar_valor_da_moeda_escolhida()
                aviso['fg'] = '#3CB371'
                aviso['text'] = f'Moeda alterada para {self.moeda_escolhida} com sucesso!'
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro,escolha umas das\n moedas disponivel!'

    def mudar_valor_da_moeda_escolhida(self):
        for m, v in self.moedas:
            if self.moeda_escolhida == m:
                self.valor_moeda = v

    def mudar_valor(self):
        try:
            real = valor.get()
            real = float(real)
            self.usuario_real = real
            aviso1['fg'] = '#3CB371'
            aviso1['text'] = f'Valor alterado para {self.usuario_real:.2f} com sucesso!'
        except:
            aviso1['fg'] = 'red'
            aviso1['text'] = 'Erro,digite da \nforma que se pede acima!'


    def real_para_moeda(self):
        try:
            result = self.usuario_real / float(self.valor_moeda)
            mostrar1['fg'] = '#363636'
            mostrar1['text'] = f'R${self.usuario_real:.2f} = {result:.2f}'
        except:
            mostrar1['fg'] = 'red'
            mostrar1['text'] = 'Algo deu errado :('


    def moeda_para_real(self):
        try:
            result = float(self.valor_moeda) * self.usuario_real
            mostrar2['fg'] = '#363636'
            mostrar2['text'] = f'{self.usuario_real:.2f} = R${result:.2f}'
        except:
            mostrar2['fg'] = 'red'
            mostrar2['text'] = 'Algo deu errado :('


janela = tk.Tk()
conversor = ConversorDeMoedas()
numeros = [c for c in range(1, 1001)]
janela.title('Conversor de Moedas &')
janela.configure(bg='#C0C0C0')

titulo_pagina = tk.Label(text='Sistema de Conversão de Moedas', borderwidth=4, relief='ridge', bg='#A9A9A9', fg='#1C1C1C')
titulo_pagina.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Escolha aqui entre as moedas disponievis', bg='#C0C0C0', fg='#363636')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

moeda = ttk.Combobox(values=conversor.moedas_disponiveis)
moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#C0C0C0', fg='#363636')
aviso.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_moeda = tk.Button(text='Mudar Moeda', bg='#696969', command=conversor.mudar_moeda)
botao_mudar_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

titulo = tk.Label(text='Valor que deseja saber em real (ex:5674.99)', borderwidth=4, relief='ridge', bg='#A9A9A9', fg='#1C1C1C')
titulo.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

valor = ttk.Combobox(values=numeros)
valor.grid(row=4, column=0, padx=10, pady=10, sticky='nswe')

aviso1 = tk.Label(text='', bg='#C0C0C0')
aviso1.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_valor = tk.Button(text='Mudar valor', bg='#696969', command=conversor.mudar_valor)
botao_mudar_valor.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

titulo1 = tk.Label(text='Real para moeda', borderwidth=4, relief='ridge', bg='#A9A9A9', fg='#1C1C1C')
titulo1.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mostrar1 = tk.Label(text='', bg='#C0C0C0', fg='#363636')
mostrar1.grid(row=7, column=0, columnspan=1, padx=10, pady=10, sticky='nswe')

botao_mudar_moeda1 = tk.Button(text='Ver conversão', bg='#696969', command=conversor.real_para_moeda)
botao_mudar_moeda1.grid(row=7, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Moeda para real', borderwidth=4, relief='ridge', bg='#A9A9A9', fg='#1C1C1C')
titulo2.grid(row=8, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mostrar2 = tk.Label(text='', bg='#C0C0C0', fg='#363636')
mostrar2.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_moeda2 = tk.Button(text='Ver conversão', bg='#696969', command=conversor.moeda_para_real)
botao_mudar_moeda2.grid(row=9, column=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar Sistema', bg='#4F4F4F', command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
