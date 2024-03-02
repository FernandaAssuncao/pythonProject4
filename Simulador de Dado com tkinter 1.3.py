from random import randint
from tkinter import ttk
import tkinter as tk


class SimuladorDeDado:
    @staticmethod
    def quantidades_d():
        lista = []
        for c in range(1, 11):
            lista.append(c)
        return lista

    def __init__(self):
        self.dado = None
        self.quantidade = 1
        self.texto = ''
        self.numeros_dado = []
        self.quantidades_disponiveis = self.quantidades_d()

    def gerar_dados_e_mostrar(self):
        self.texto = ''
        for c in range(1, self.quantidade + 1):
            self.dado = randint(1, 6)
            self.texto += f'{c}º dado caiu {self.dado}\n'
        mostrar_dado['text'] = f'{self.texto}'

    def girar_dado(self):
        try:
           self.gerar_dados_e_mostrar()
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, faça\n o que se pede!'

    def mudar_quantidade(self):
        try:
            quantidade = quant.get()
            quantidade = int(quantidade)
            self.quantidade = quantidade
            aviso['fg'] = '#FFB6C1'
            aviso['text'] = f'Quantidade de vezes\n que o dado vai gira\n alterado para {self.quantidade}\n com sucesso!'
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, por favor\n digite o que se pede!'


simulador = SimuladorDeDado()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFE4E1')

titulo = tk.Label(text='Simulador de\n Dado', borderwidth=4, relief='ridge', bg='#FFB6C1', fg='white',
                  font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mostrar_dado = tk.Label(text='', bg='#FFE4E1', fg='#FFB6C1', font='Arial 13 bold')
mostrar_dado.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_girar_dado = tk.Button(text='Girar Dado', bg='#FFB6C1', fg='white', font='Arial 15 bold',
                             command=simulador.girar_dado)
botao_girar_dado.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Quantas vezes o\n dado vai girar?', bg='#FFE4E1', fg='#FFB6C1', font='Arial 10 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

quant = ttk.Combobox(values=simulador.quantidades_disponiveis)
quant.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFE4E1', fg='#FFB6C1', font='Arial 10 bold')
aviso.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_tiros = tk.Button(text='Mudar quantidade', bg='#FFB6C1', fg='white', font='Arial 15 bold',
                              command=simulador.mudar_quantidade)
botao_mudar_tiros.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
