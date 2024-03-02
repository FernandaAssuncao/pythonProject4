from tkinter import ttk
import tkinter as tk


class Tabuada:
    def __init__(self):
        self.numero = None
        self.tabuada = []
        self.texto = ''
        self.numeros_disponiveis = []
        self.__adicionar_numeros()

    def __adicionar_numeros(self):
        for c in range(1, 1001):
            self.numeros_disponiveis.append(c)

    def mudar_numero(self):
        try:
            if len(self.tabuada) != 0:
                self.tabuada.clear()
                self.texto = ''
            numeroo = numero.get()
            numeroo = int(numeroo)
            self.numero = numeroo
            self.__editar_tabuada()
            self.__editar_texto()
            mostrar_numero['text'] = f'Tabuada do.....{self.numero}'
            aviso['fg'] = '#008080'
            aviso['text'] = f'Número alterado para\n {self.numero} com sucesso!'
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro,digite o que se pede!'

    def __editar_tabuada(self):
        for c in range(1, 11):
            self.tabuada.append(self.numero * c)

    def __editar_texto(self):
        for c in range(1, 11):
            self.texto += f'{self.numero} X {c} = {self.tabuada[c - 1]}\n'

    def mostrar_tabuada(self):
        try:
            numero1['text'] = f'{self.texto}'
        except:
            aviso2['fg'] = 'red'
            aviso2['text'] = "Não foi pesquisar a tabuada"


tabu = Tabuada()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#B0E0E6')

titulo = tk.Label(text='Gerador de \nTabuadas', borderwidth=4, relief='raised', bg='#87CEEB', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Digite o número aqui', bg='#B0E0E6', fg='#008080',
                    font='Arial 8 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

numero = ttk.Combobox(values=tabu.numeros_disponiveis)
numero.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#B0E0E6', fg='#008080')
aviso.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_numero = tk.Button(text='Mudar número', bg='#87CEFA', fg='white',
                               font='Arial 10 bold', command=tabu.mudar_numero)
botao_mudar_numero.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

mostrar_numero = tk.Label(text='Tabuada do.....', borderwidth=4, relief='raised', bg='#87CEEB', fg='white',
                          font='Arial 15 bold')
mostrar_numero.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

numero1 = tk.Label(text='', bg='#87CEEB', fg='#0000FF')
numero1.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

aviso2 = tk.Label(text='', bg='#B0E0E6', fg='#008080')
aviso2.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_ver_tabuada = tk.Button(text='Mostrar Tabuada', bg='#87CEFA', fg='white', font='Arial 10 bold',
                              command=tabu.mostrar_tabuada)
botao_ver_tabuada.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
