from math import sqrt
from tkinter import ttk
import tkinter as tk


class Matematicando:
    @staticmethod
    def sortear_numeros(quantidade=1000):
        lista = []
        for c in range(1, quantidade + 1):
            lista.append(c)
        return lista

    def __init__(self):
        self.numero = None
        self.divisores = []
        self.primo_ou_nao = None
        self.raiz_quadrada = None
        self.texto = ''
        self.numeros_disponiveis = []
        self.__adicionar_a_lista()

    def __adicionar_a_lista(self):
        self.numeros_disponiveis = self.sortear_numeros(quantidade=500)

    def mudar_numero(self):
        try:
            if len(self.divisores) != 0:
                self.divisores.clear()
            num = numero.get()
            num = int(num)
            self.numero = num
            self.mudar_texto()
            self.__adicionar_divisores()
            self.__primo_ou_nao_primo()
            self.__text_div()
            self.__calcular_raiz_quadrada()
            aviso['fg'] = 'white'
            aviso['text'] = f'Número alterado para \n{self.numero} com sucesso!'
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro,digite um número\n INTEIRO VALIDO'

    def __adicionar_divisores(self):
        for c in range(self.numero, 0, -1):
            if self.numero % c == 0:
                self.divisores.append(c)

    def __text_div(self):
        for n in self.divisores:
            self.texto = f'{self.texto}' + f'{n}, '

    def __primo_ou_nao_primo(self):
        if len(self.divisores) == 2:
            self.primo_ou_nao = 'É PRIMO'
        else:
            self.primo_ou_nao = 'NÃO É PRIMO'

    def __calcular_raiz_quadrada(self):
        self.raiz_quadrada = sqrt(self.numero)

    def mudar_texto(self):
        self.texto = f'Os divisores de {self.numero}\n são '

    def mostrar_raiz_quadrada(self):
        aviso2['text'] = f'{self.raiz_quadrada:.1f}'

    def mostrar_primo(self):
        aviso3['text'] = f'O número {self.numero}\n {self.primo_ou_nao}'

    def mostrar_divisores(self):
        aviso4['text'] = f'{self.texto}'

    def iniciar(self):
        try:
            self.mostrar_raiz_quadrada()
            self.mostrar_primo()
            self.mostrar_divisores()
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro,algo deu errado!'


janela = tk.Tk()
mat = Matematicando()
janela.title('')
janela.configure(bg='#FFE4B5')

titulo = tk.Label(text='Matematicando', borderwidth=4, relief='raised', bg='#FF7F50', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Escolha um número aqui', bg='#FFE4B5', fg='#FF4500', font='Arial 8 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

numero = ttk.Combobox(values=mat.numeros_disponiveis)
numero.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFA07A', fg='white', font='Arial 8 bold')
aviso.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_numero = tk.Button(text='Mudar Número', bg='#FF7F50', fg='white', font='Arial 10 bold',
                               command=mat.mudar_numero)
botao_mudar_numero.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Raiz Quadrada', borderwidth=4, relief='ridge', bg='#FF7F50', fg='white',
                   font='Arial 12 bold')
titulo2.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

aviso2 = tk.Label(text='', bg='#FFA07A', fg='white', font='Arial 8 bold')
aviso2.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

titulo3 = tk.Label(text='Primo ou não?', borderwidth=4, relief='ridge', bg='#FF7F50', fg='white',
                   font='Arial 12 bold')
titulo3.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

aviso3 = tk.Label(text='', bg='#FFA07A', fg='white', font='Arial 8 bold')
aviso3.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

titulo4 = tk.Label(text='Divisores', borderwidth=4, relief='ridge', bg='#FF7F50', fg='white',
                   font='Arial 12 bold')
titulo4.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

aviso4 = tk.Label(text='', bg='#FFA07A', fg='white', font='Arial 8 bold')
aviso4.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar', bg='#FF7F50', fg='white', font='Arial 10 bold',
                         command=janela.quit)
botao_fechar.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mostrar_tudo = tk.Button(text='Iniciar', bg='#FF7F50', fg='white', font='Arial 10 bold',
                               command=mat.iniciar)
botao_mostrar_tudo.grid(row=6, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
