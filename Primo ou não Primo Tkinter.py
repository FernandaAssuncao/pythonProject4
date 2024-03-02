from tkinter import ttk
import tkinter as tk


class PrimoOuNaoPrimo:
    def __init__(self):
        self.numero = None
        self.divisores = []
        self.primo_ou_nao = ''
        self.lista_de_numeros = []
        self.adicionar_lista_numeros()

    def adicionar_lista_numeros(self):
        for c in range(1, 1001):
            self.lista_de_numeros.append(c)

    def mudar_numero(self):
        numero = num.get()
        try:
            if len(self.divisores) != 0:
                self.divisores.clear()
            self.numero = int(numero)
            mensagem_positivo['foreground'] = '#00FA9A'
            mensagem_positivo['text'] = f'Número alterado \npara {self.numero} com sucesso!'
            self.__quais_divisores()
            self.__e_primo_ou_nao()
        except:
            mensagem_positivo['foreground'] = '#FF0000'
            mensagem_positivo['text'] = 'Digite um número INTEIRO valido'

    def __quais_divisores(self):
        for c in range(self.numero, 0, -1):
            if self.numero % c == 0:
                self.divisores.append(c)

    def mostrar_divisores(self):
        mensagem_divisores['text'] = f'Os divisores de {self.numero}\n são {self.divisores}'

    def __e_primo_ou_nao(self):
        if len(self.divisores) == 2:
            self.primo_ou_nao = 'É PRIMO'
        else:
            self.primo_ou_nao = 'NÃO É PRIMO'

    def mostrar_primo_ou_nao(self):
        mensagem_primo_ou_nao['text'] = f'O número {self.numero} {self.primo_ou_nao}'


primo = PrimoOuNaoPrimo()
janela = tk.Tk()
janela.title('Primo ou não Primo?')
janela.configure(background='#FFE4C4')

titulo = tk.Label(text='Mudar número', borderwidth=2, relief='solid', background='#FF7F50', foreground='black')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Digite um número aqui', background='#FFE4C4', foreground='#FF7F50')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

num = ttk.Combobox(values=primo.lista_de_numeros)
num.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem_positivo = tk.Label(text='', background='#FFE4C4', foreground='#00FA9A')
mensagem_positivo.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_numero = tk.Button(text='Mudar número', background='#FF4500', foreground='black', command=primo.mudar_numero)
botao_mudar_numero.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Divisores', borderwidth=2, relief='solid', background='#FF7F50', foreground='black')
titulo2.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem_divisores = tk.Label(text='Divisores do número escolhido', background='#FFE4C4', foreground='#FF7F50')
mensagem_divisores.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_divisores = tk.Button(text='Ver divisores', background='#FF4500', foreground='black', command=primo.mostrar_divisores)
botao_divisores.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

titulo3 = tk.Label(text='Primo ou não Primo?', borderwidth=2, relief='solid', background='#FF7F50', foreground='black')
titulo3.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem_primo_ou_nao = tk.Label(text='Primo ou não?', background='#FFE4C4', foreground='#FF7F50')
mensagem_primo_ou_nao.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_primo = tk.Button(text='Primo ou não', background='#FF4500', foreground='black', command=primo.mostrar_primo_ou_nao)
botao_primo.grid(row=6, column=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar', background='#FFA07A', foreground='black', command=janela.quit)
botao_fechar.grid(row=7, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
