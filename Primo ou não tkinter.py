from tkinter import ttk
import tkinter as tk


class PrimoOuNao:
    @staticmethod
    def adicionar_numero():
        lista = []
        for c in range(1, 2001):
            lista.append(c)
        return lista

    def __init__(self):
        self.numero = None
        self.divisores = []
        self.primo_ou_nao = None
        self.numeros_disponiveis = self.adicionar_numero()

    def deletar_divisores(self):
        self.divisores.clear()
        self.primo_ou_nao = None

    def adicionar_divisores(self):
        for c in range(1, self.numero + 1):
            if self.numero % c == 0:
                self.divisores.append(c)

    def e_primo_ou_nao(self):
        if len(self.divisores) == 2:
            self.primo_ou_nao = 'É PRIMO'
        else:
            self.primo_ou_nao = 'NÃO É PRIMO'

    def mostrar_resultados(self):
        mensagem['fg'] = 'white'
        mensagem['text'] = f'Os divisores de {self.numero} são {self.divisores}\n{self.primo_ou_nao}'

    def analisar_primo_ou_nao(self):
        try:
            self.deletar_divisores()
            num = numero.get()
            num = int(num)
            self.numero = num
            self.adicionar_divisores()
            self.e_primo_ou_nao()
            self.mostrar_resultados()
        except:
            mensagem['fg'] = 'red'
            mensagem['text'] = 'ERRO, faça o que se pede!!!'


primo = PrimoOuNao()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFC0CB')

titulo = tk.Label(text='Primo ou não?', borderwidth=4, relief='raised', bg='#FFB6C1', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='Digite aqui um número', bg='#FFC0CB', fg='white', font='Arial 12 bold')
aviso.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

numero = ttk.Combobox(values=primo.numeros_disponiveis)
numero.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='', bg='#FFC0CB', fg='#FFB6C1', font='Arial 12 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_calcular = tk.Button(text='É PRIMO OU NÃO', bg='#FFB6C1', fg='white',
                           font='Arial 13 bold', command=primo.analisar_primo_ou_nao)
botao_calcular.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
