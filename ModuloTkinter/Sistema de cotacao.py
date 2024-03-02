import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import requests


requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requisicao.json()


lista_moedas = list(dicionario_moedas.keys())


def pegar_cotacao():
    moeda = combox_selecionar_moeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]['bid']
    label_textocotacao['text'] = f'A cotação foi de: R${valor_moeda}'


janela = tk.Tk()

janela.title('Ferramenta de Cotação de Moedas')

label_cotacaomoeda = tk.Label(text='Cotação de 1 moeda especifica', borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)


label_selecionarmoeda = tk.Label(text='Selecionar Moeda', anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combox_selecionar_moeda = ttk.Combobox(values=lista_moedas)
combox_selecionar_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionardia = tk.Label(text='Selecione o dia que deseja pegar a cotação', anchor='e')
label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

calendario_moeda = DateEntry(year=2022, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

label_textocotacao = tk.Label(text='')
label_textocotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_pegar_cotacao = tk.Button(text='Pegar Cotação', command=pegar_cotacao)
botao_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar', command=janela.quit)
botao_fechar.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
