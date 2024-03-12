from random import randint
import tkinter as tk


class GeradorDeMatrix:
    def __init__(self):
        self.matrix = []
        self.texto = ''

    def excluir_matrix_antiga(self):
        if len(self.matrix) != 0:
            self.matrix.clear()
            self.texto = ''

    def gerar_matrix(self):
        lista = []
        for c in range(0, 3):
            for i in range(0, 3):
                lista.append(randint(1, 9))
            self.matrix.append(lista[:])
            lista.clear()

    def editar_texto(self):
        for c in range(0, 3):
            for i in range(0, 3):
                self.texto += f'[ {self.matrix[c][i]} ] '
            self.texto += '\n'

    def mudar_mensagem(self):
        mensagem['fg'] = 'white'
        mensagem['text'] = f'{self.texto}'

    def mostrar_matrix(self):
        try:
            self.excluir_matrix_antiga()
            self.gerar_matrix()
            self.editar_texto()
            self.mudar_mensagem()
        except:
            mensagem['fg'] = 'red'
            mensagem['text'] = 'Erro, faça tudo o que se pede!!'


gerador = GeradorDeMatrix()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFC0CB')

titulo = tk.Label(text='Gerador de Matrix', borderwidth=4, relief='raised', bg='#FFB6C1',
                  fg='white', font='Arial 16 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='', bg='#FFB6C1', fg='white', font='Arial 10 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_gerar_matrix = tk.Button(text='Gerar Matrix', bg='#FFB6C1', fg='white',
                               font='Arial 13 bold', command=gerador.mostrar_matrix)
botao_gerar_matrix.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
