from tkinter import ttk
import tkinter as tk


class GeradorDeTabuadas:
    @staticmethod
    def adicionar_numeros():
        lista = []
        for c in range(1, 1001):
            lista.append(c)
        return lista

    def __init__(self):
        self.numero = None
        self.tabuada = []
        self.texto = ''
        self.numeros_disponiveis = self.adicionar_numeros()

    def geradorr(self):
        try:
            nume = num.get()
            nume = int(nume)
            self.numero = nume
            self.gerar_tabuada()
            self.mostrar_texto()
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, faça\n o que se pede!'

    def __apagar_tabuada(self):
        self.tabuada.clear()

    def gerar_tabuada(self):
        self.__apagar_tabuada()
        self.excluir_texto()
        for c in range(1, 11):
            self.tabuada.append(self.numero * c)

    def __fazer_texto(self):
        for c in range(1, 11):
            self.texto += f'{self.numero} X {c} = {self.tabuada[c -1]}\n'

    def excluir_texto(self):
        self.texto = ''

    def mostrar_texto(self):
        self.__fazer_texto()
        mostrar['text'] = f'{self.texto}'


gerador = GeradorDeTabuadas()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFE4E1')

titulo = tk.Label(text='Sistema de\n Tabuadas', borderwidth=4, relief='ridge', bg='#FFB6C1', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Digite um\n número aqui ->', bg='#FFE4E1', fg='#FFB6C1', font='Arial 10 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

num = ttk.Combobox(values=gerador.numeros_disponiveis)
num.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Tabuada do ?', borderwidth=4, relief='raised', bg='#FFB6C1', fg='white',
                   font='Arial 14 bold')
titulo2.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='nswe')

mostrar = tk.Label(text='', bg='#FFB6C1', fg='white', font='Arial 10 bold')
mostrar.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFE4E1', fg='#FFB6C1', font='Arial 12 bold')
aviso.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mostrar_tabuada = tk.Button(text='Ve Tabuada', bg='#FFB6C1', fg='white', font='Arial 12 bold',
                                  command=gerador.geradorr)
botao_mostrar_tabuada.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
