import tkinter as tk
from tkinter import ttk


janela = tk.Tk()
janela.title('Cotação de Moedas')

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text='Sistema de busca de cotações de moedas', fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky='EW')

mensagem2 = tk.Label(text='Selecione a Moeda desejada')
mensagem2.grid(row=1, column=0)

# moeda = tk.Entry()
# moeda.grid(row=1, column=1)

dicionario_cotacoes = {'Dólar': 5.47,
                       'Euro': 5.50,
                       'Bitcoin': 20.000}

moedas = list(dicionario_cotacoes.keys())

moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)


def buscar_cotacao():
    moeda_preencida = moeda.get()
    cotacao = dicionario_cotacoes.get(moeda_preencida)
    mensagem_cotacao = tk.Label(text='Cotação não encontrada')
    mensagem_cotacao.grid(row=3, column=1)
    if cotacao:
        mensagem_cotacao['text'] = f'Cotação do {moeda_preencida} é de {cotacao} reais!'



botao = tk.Button(text='Buscar Cotação', command=buscar_cotacao)
botao.grid(row=2, column=1)

mensagem3 = tk.Label(text='Caso queira pegar mais de uma cotação ao mesmo tempo digite uma moeda em cada linha')
mensagem3.grid(row=4, column=0, columnspan=2)

caixa_texto = tk.Text(width=10, height=5)
caixa_texto.grid(row=5, column=0, sticky='nswe')


def buscar_cotacoes():
    texto = caixa_texto.get('1.0', tk.END)
    lista_moedas = texto.split('\n')
    mensagem_cotacoes = []
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f'{item}: {cotacao}')
    mensagem4 = tk.Label(text='\n'.join(mensagem_cotacoes))
    mensagem4.grid(row=6, column=1)


botao_multiplas = tk.Button(text='Buscar Cotações', command=buscar_cotacoes)
botao_multiplas.grid(row=5, column=1)

janela.mainloop()
