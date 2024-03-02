from tkinter import ttk
import requests
import tkinter as tk


link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'


class ConversorMoedas:
    def __init__(self):
        self.moeda_escolhida = None
        self.cotacao = None
        self.lista_de_moedas = []
        self.lista_de_cotacoes = []
        self.adicionar_moedas()

    def adicionar_moedas(self):
        requisicao = requests.get(f'{link}')
        dic = requisicao.json()
        for item in dic:
            self.lista_de_moedas.append(item)
            self.lista_de_cotacoes.append((item, dic[item]))

    def mudar_moeda(self):
        escolha = usuario.get()
        if escolha in self.lista_de_moedas:
            self.moeda_escolhida = escolha
            conplemento['foreground'] = 'green'
            conplemento['text'] = f'Moeda alterada para {self.moeda_escolhida}\n com sucesso'
            for moeda, dic in self.lista_de_cotacoes:
                if moeda == self.moeda_escolhida:
                    self.cotacao = dic['bid']
                    self.cotacao = float(self.cotacao)
        else:
            conplemento['foreground'] = 'red'
            conplemento['text'] = 'Moeda não disponivel'

    def mudar_real(self):
        try:
            real = usuario1.get()
            real = float(real)
            valor_da_moeda = real / self.cotacao
            valor_final['foreground'] = 'black'
            valor_final['text'] = f'R${real:.2f} = {valor_da_moeda:.2f}'
        except:
            valor_final['foreground'] = 'red'
            valor_final['text'] = 'Erro,digite um \nformato de moeda valida'


janela = tk.Tk()
sistema = ConversorMoedas()
janela.configure(background='#7FFFD4')
janela.title('Sistema de Conversão')

titulo = tk.Label(text='Conversor de Moedas', borderwidth=2, relief='solid', background='#20B2AA', foreground='black')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Escolha uma das moedas', background='#7FFFD4', foreground='#008080')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

usuario = ttk.Combobox(values=sistema.lista_de_moedas)
usuario.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

conplemento = tk.Label(text='', background='#7FFFD4')
conplemento.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_moeda = tk.Button(text='Mudar moeda', background='#48D1CC', command=sistema.mudar_moeda)
botao_mudar_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

mensagem2 = tk.Label(text=f'Converter REAL para a moeda escolhida', borderwidth=2, relief='solid', background='#20B2AA', foreground='black')
mensagem2.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

texto = tk.Label(text='Digite o valor EM REAL aqui\n(Digite no lugar da virgula um PONTO)\npor exemplo 5674.99', background='#7FFFD4', foreground='#008080')
texto.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

usuario1 = ttk.Combobox(values=[i for i in range(1, 10000)])
usuario1.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

valor_final = tk.Label(text='', background='#7FFFD4')
valor_final.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_buscar_valor = tk.Button(text='Buscar Valor', background='#48D1CC', command=sistema.mudar_real)
botao_buscar_valor.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar Sistema', background='#48D1CC', command=janela.quit)
botao_fechar.grid(row=6, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
