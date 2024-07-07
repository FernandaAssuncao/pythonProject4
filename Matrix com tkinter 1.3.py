from random import randint
import tkinter as tk


class GeradorDeMatriz:
    def __init__(self):
        self.matrix = []
        self.texto = ''

    def __excluir_matrix_antiga(self):
        self.matrix.clear()
        self.texto = ''

    def __criar_matrix(self):
        lista = []
        for c in range(0, 3):
            for i in range(0, 3):
                lista.append(randint(1, 9))
            self.matrix.append(lista[:])
            lista.clear()

    def __analisar_situacao(self):
        if len(self.matrix) != 0:
            self.__excluir_matrix_antiga()

    def __mudar_texto(self):
        for c in range(0, 3):
            for i in range(0, 3):
                self.texto += f'[{self.matrix[c][i]}] '
            self.texto += '\n'

    def __mostrar_texto_definitivo(self):
        mensagem['fg'] = 'white'
        mensagem['text'] = f'{self.texto}'

    def comecar(self):
        try:
            self.__analisar_situacao()
            self.__criar_matrix()
            self.__mudar_texto()
            self.__mostrar_texto_definitivo()
        except:
            mensagem['fg'] = 'red'
            mensagem['text'] = 'Erro, por favor\n faça o que se pede!!'


gerador = GeradorDeMatriz()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFC0CB')

titulo = tk.Label(text='Gerador de Matrix', bg='#FFB6C1', borderwidth=4, relief='raised', fg='white',
                  font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='', bg='#FFC0CB', fg='white', font='Arial 12 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_gerar_matrix = tk.Button(text='Gerar Matrix', bg='#FFB6C1', fg='white', font='Arial 15 bold',
                               command=gerador.comecar)
botao_gerar_matrix.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
