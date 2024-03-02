from random import randint
from tkinter import ttk
import tkinter as tk


class GeradorDeMatrix:
    @staticmethod
    def adicionar_numeros():
        lista = []
        for c in range(1, 10):
            lista.append(c)
        return lista

    def __init__(self):
        self.matrix = []
        self.texto = ''
        self.aposta = None
        self.numeros_disponiveis = self.adicionar_numeros()

    def __gerar_matrix(self):
        self.veficar_matrix_antiga()
        lista = []
        for c in range(0, 3):
            for i in range(0, 3):
                lista.append(randint(1, 9))
            self.matrix.append(lista[:])
            lista.clear()

    def __excluir_matrix_antiga(self):
        self.matrix.clear()
        self.texto = ''

    def veficar_matrix_antiga(self):
        if len(self.matrix) != 0:
            self.__excluir_matrix_antiga()

    def __mostrar_matrix(self):
        for c in range(0, 3):
            for i in range(0, 3):
                self.texto += f'[ {self.matrix[c][i]} ] '
            self.texto += '\n'

    def atualizar_texto(self):
        mostrar['text'] = f'{self.texto}'

    def funcao_gerar_matrix(self):
        try:
            self.__gerar_matrix()
            self.__mostrar_matrix()
            self.atualizar_texto()
            self.veficar_valor_aposta()
        except:
            pass

    def veficar_valor_aposta(self):
        if self.aposta is not None:
            if self.aposta == self.matrix[0][0]:
                aviso['fg'] = 'white'
                aviso['text'] = 'Parabens você\n acertou!'
            else:
                aviso['fg'] = 'white'
                aviso['text'] = 'Não foi\n dessa vez!'

    def apostar_valor(self):
        try:
            num = aposte.get()
            num = int(num)
            if num in self.numeros_disponiveis:
                self.aposta = num
                aviso['fg'] = 'white'
                aviso['text'] = f'Número {self.aposta}\n apostado com sucesso!'
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, faça\n o que se pede!'


gerador = GeradorDeMatrix()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFF0F5')

titulo = tk.Label(text='Gerador de\n Matrix', borderwidth=4, relief='ridge', bg='#FFE4E1', fg='white',
                  font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mostrar = tk.Label(text='', bg='#FFE4E1', fg='white', font='Arial 12 bold')
mostrar.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mostrar = tk.Button(text='Gerar Matrix', bg='#FFE4E1', fg='white', font='Arial 15 bold',
                          command=gerador.funcao_gerar_matrix)
botao_mostrar.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Apostar valor', borderwidth=4, relief='ridge', bg='#FFE4E1', fg='white',
                   font='Arial 20 bold')
titulo2.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Aposte o valor q\n vc acha q vai cair \n [ ? ] [ 1 ] [ 2 ]\n [ 3 ] [ 4 ] [ 5 ]\n [ 6 ] [ 7 ] [ 8 ]',
                    bg='#FFE4E1', fg='white', font='Arial 12 bold')
mensagem.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

aposte = ttk.Combobox(values=gerador.numeros_disponiveis)
aposte.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFE4E1', fg='white', font='Arial 12 bold')
aviso.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_apostar = tk.Button(text='Apostar', bg='#FFE4E1', fg='white', font='Arial 15 bold',
                          command=gerador.apostar_valor)
botao_apostar.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
