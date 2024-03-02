from tkinter import ttk
from math import sqrt
import tkinter as tk


class Matematica:
    def __init__(self):
        self.numero = 0
        self.par = None
        self.primo_ou_nao = None
        self.raiz_quadrada = None
        self.divisores = []

    def mudar_numero(self):
        try:
            if len(self.divisores) != 0:
                self.divisores.clear()
            numero = mudar_numero.get()
            numero = int(numero)
            self.numero = numero
            self.__quais_divisores()
            self.__e_par_ou_impar()
            self.__primo_ou_nao_primo()
            self.__raiz_quadrada()
            mensagem_mudar_numero['foreground'] = 'black'
            mensagem_mudar_numero['text'] = f'Número alterado para {self.numero} \ncom sucesso!'
        except:
            mensagem_mudar_numero['foreground'] = 'red'
            mensagem_mudar_numero['text'] = 'Erro,por favor digite\num número VALÍDO'

    def __quais_divisores(self):
        if self.numero is not None:
            for c in range(self.numero, 0, -1):
                if self.numero % c == 0:
                    self.divisores.append(c)

    def __e_par_ou_impar(self):
        if 2 in self.divisores:
            self.par = 'PAR'
        else:
            self.par = 'IMPAR'

    def mostrar_par_ou_impar(self):
        mensagem_par_ou_impar['text'] = f'O número {self.numero} é {self.par}'

    def __primo_ou_nao_primo(self):
        if len(self.divisores) == 2:
            self.primo_ou_nao = 'É PRIMO'
        else:
            self.primo_ou_nao = 'NÃO É PRIMO'

    def mostrar_primo_ou_nao_primo(self):
        mensagem_primo_ou_nao_primo['text'] = f'O número {self.numero} {self.primo_ou_nao}'

    def __raiz_quadrada(self):
        self.raiz_quadrada = sqrt(self.numero)

    def mostrar_raiz_quadrada(self):
        mensagem_raiz_quadrada['text'] = f'A raiz quadrada de {self.numero} é {self.raiz_quadrada:.1f}'


janela = tk.Tk()
mat = Matematica()
janela.configure(background='pink')
janela.title('Matematica')

titulo = tk.Label(text='Matematica', borderwidth=2, relief='ridge', background='black', foreground='pink')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='   Digite um número aqui  --->  ', background='black', foreground='pink')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

mudar_numero = ttk.Combobox(values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mudar_numero.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem_mudar_numero = tk.Label(text='Número alterado ou não?', background='pink')
mensagem_mudar_numero.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_numero = tk.Button(text='Mudar número', background='black', foreground='pink', command=mat.mudar_numero)
botao_mudar_numero.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')


titulo2 = tk.Label(text='Par ou Impar', borderwidth=2, relief='ridge', background='black', foreground='pink')
titulo2.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem_par_ou_impar = tk.Label(text='O número é par ou impar?', background='pink')
mensagem_par_ou_impar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_par_ou_impar = tk.Button(text='Par ou Impar?', background='black', foreground='pink', command=mat.mostrar_par_ou_impar)
botao_par_ou_impar.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')


titulo3 = tk.Label(text='Primo ou não primo', borderwidth=2, relief='ridge', background='black', foreground='pink')
titulo3.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem_primo_ou_nao_primo = tk.Label(text='É primo ou não primo?', background='pink')
mensagem_primo_ou_nao_primo.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_primo_ou_nao_primo = tk.Button(text='Primo ou Não Primo?', background='black', foreground='pink', command=mat.mostrar_primo_ou_nao_primo)
botao_primo_ou_nao_primo.grid(row=6, column=2, padx=10, pady=10, sticky='nswe')


titulo4 = tk.Label(text='Raiz Quadrada', borderwidth=2, relief='ridge', background='black', foreground='pink')
titulo4.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem_raiz_quadrada = tk.Label(text='Qual Raiz Quadrada?', background='pink')
mensagem_raiz_quadrada.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_raiz_quadrada = tk.Button(text='Qual Raiz quadrada?', background='black', foreground='pink', command=mat.mostrar_raiz_quadrada)
botao_raiz_quadrada.grid(row=8, column=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar', background='black', foreground='pink', command=janela.quit)
botao_fechar.grid(row=9, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
