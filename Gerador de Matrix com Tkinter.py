from random import randint
import tkinter as tk


class GeradorMatrix:
    def __init__(self):
        self.matrix = []
        self.texto = ''

    def __gerar_matrix(self):
        self.__excluir_matrix_texto()
        lista = []
        for c in range(0, 3):
            for i in range(0, 3):
                lista.append(randint(1, 9))
            self.matrix.append(lista[:])
            lista.clear()

    def mostrar_matrix(self):
        for c in range(0, 3):
            for i in range(0, 3):
                self.texto += f'[ {self.matrix[c][i]} ] '
            self.texto += '\n'
        mostrar['text'] = f'{self.texto}'

    def __excluir_matrix_texto(self):
        self.matrix.clear()
        self.texto = ''

    def funcao(self):
        try:
            self.__gerar_matrix()
            self.mostrar_matrix()
        except:
            pass


gerador = GeradorMatrix()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFEBCD')

titulo = tk.Label(text='Gerador de\n Matrix', borderwidth=4, relief='raised', bg='#FFDEAD', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mostrar = tk.Label(text='', bg='#FFDEAD', fg='white', font='Arial 12 bold')
mostrar.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar = tk.Button(text='Gerar Matrix', bg='#FFDEAD', fg='white', font='Arial 13 bold',
                        command=gerador.funcao)
botao_mudar.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
