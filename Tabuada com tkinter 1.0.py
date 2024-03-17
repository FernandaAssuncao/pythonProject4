from tkinter import ttk
import tkinter as tk


class Tabuada:
    @staticmethod
    def __adicionar_numeros():
        lista = []
        for c in range(1, 2001):
            lista.append(c)
        return lista

    def __init__(self):
        self.numero = None
        self.tabuada = []
        self.texto = ''
        self.numeros_disponiveis = self.__adicionar_numeros()

    def __excluir_tabuada_antiga(self):
        if len(self.tabuada) != 0:
            self.tabuada.clear()
            self.texto = ''

    def __calcular_tabuada(self):
        for c in range(1, 11):
            self.tabuada.append(self.numero * c)

    def __editar_texto(self):
        for c in range(1, 11):
            self.texto += f'{c} X {self.numero} = {self.tabuada[c - 1]}\n'

    def editar_mensagem(self):
        mensagem['fg'] = 'white'
        mensagem['text'] = f'{self.texto}'

    def mostrar_tabuada(self):
        try:
            self.__excluir_tabuada_antiga()
            num = numero.get()
            num = int(num)
            self.numero = num
            self.__calcular_tabuada()
            self.__editar_texto()
            self.editar_mensagem()
        except:
            mensagem['fg'] = 'red'
            mensagem['text'] = 'Erro, Por favor\n faça o que se pede!!'


tabuada = Tabuada()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFE4C4')

titulo = tk.Label(text='Tabuadas', borderwidth=4, relief='raised', bg='#FFDAB9', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='Digite aqui um número\n para saber a sua tabuada', bg='#FFE4C4',
                 fg='white', font='Arial 12 bold')
aviso.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

numero = ttk.Combobox(values=tabuada.numeros_disponiveis)
numero.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='', bg='#FFDAB9', fg='white', font='Arial 12 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_ver_tabuada = tk.Button(text='Ver Tabuada', bg='#FFDAB9', fg='white',
                              font='Arial 13 bold', command=tabuada.mostrar_tabuada)
botao_ver_tabuada.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
