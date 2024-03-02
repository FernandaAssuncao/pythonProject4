from tkinter import ttk
import tkinter as tk


class DescobrirDivisores:
    @staticmethod
    def adicionar_numeros():
        lista = []
        for c in range(1, 1001):
            lista.append(c)
        return lista

    def __init__(self):
        self.numero = None
        self.divisores = []
        self.texto = ''
        self.numeros_disponiveis = self.adicionar_numeros()

    def calcular_divisores(self):
        for c in range(self.numero, 0, -1):
            if self.numero % c == 0:
                self.divisores.append(c)

    def excluir_divisores(self):
        if len(self.divisores) != 0:
            self.divisores.clear()

    def editar_texto(self):
        self.texto += f'Os divisores de {self.numero}\n são '
        for c in self.divisores:
            self.texto += f'{c}, '

    def excluir_texto(self):
        self.texto = ''

    def mostrar_divisores(self):
        try:
            self.excluir_divisores()
            self.excluir_texto()
            nume = num.get()
            nume = int(nume)
            self.numero = nume
            self.calcular_divisores()
            self.editar_texto()
            mostrar['fg'] = 'white'
            mostrar['text'] = f'{self.texto}'
        except:
            mostrar['fg'] = 'red'
            mostrar['text'] = 'Erro, por favor\n digite o que se pede!'


div = DescobrirDivisores()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFEBCD')

titulo = tk.Label(text='Divisores', borderwidth=4, relief='raised', bg='#FFDAB9', fg='white',
                  font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Digite um\n número aqui', bg='#FFEBCD', fg='white', font='Arial 10 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

num = ttk.Combobox(values=div.numeros_disponiveis)
num.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mostrar = tk.Label(text='', bg='#FFDAB9', fg='white', font='Arial 12 bold')
mostrar.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mostrar_divisores = tk.Button(text='Mostrar Divisores', bg='#FFDAB9', fg='white',
                                    font='Arial 15 bold', command=div.mostrar_divisores)
botao_mostrar_divisores.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
