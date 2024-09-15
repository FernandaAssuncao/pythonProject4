from tkinter import ttk
import tkinter as tk


class Matematica:
    @staticmethod
    def __adicionar_numeros():
        lista = []
        for c in range(1, 1001):
            lista.append(c)
        return lista

    def __init__(self):
        self.numero = None
        self.primo_ou_nao = None
        self.divisores = []
        self.par_ou_impar = None
        self.numeros_disponiveis = self.__adicionar_numeros()

    def __reiniciar_tudo(self):
        if len(self.divisores) != 0:
            self.divisores.clear()

    def calcular_divisores(self):
        for c in range(1, 11):
            if self.numero % c == 0:
                self.divisores.append(c)

    def analisar_primos(self):
        if len(self.divisores) == 2:
            self.primo_ou_nao = 'É PRIMO'
        else:
            self.primo_ou_nao = 'NÃO É PRIMO'

    def analisar_par_impar(self):
        if 2 in self.divisores:
            self.par_ou_impar = 'par'
        else:
            self.par_ou_impar = 'impar'

    def mudar_texto(self):
        aviso['fg'] = 'white'
        aviso['text'] = f'Os divisores de {self.numero} são {self.divisores}\nO numero escolhido {self.primo_ou_nao}\nO numero é {self.par_ou_impar} '

    def mostrar(self):
        try:
            self.__reiniciar_tudo()
            num = numero.get()
            num = int(num)
            self.numero = num
            self.calcular_divisores()
            self.analisar_primos()
            self.analisar_par_impar()
            self.mudar_texto()
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, por favor\n faça o que se pede!!'


mat = Matematica()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFC0CB')

titulo = tk.Label(text='Matematica', borderwidth=4, relief='raised', bg='#FFC0CB', fg='white',
                  font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Digite um valor aqui: ', bg='#FFC0CB', fg='white', font='Arial 12 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

numero = ttk.Combobox(values=mat.numeros_disponiveis)
numero.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFC0CB', fg='white', font='Arial 10 bold')
aviso.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao = tk.Button(text='Mostrar Informações', bg='#FFC0CB', fg='white', font='Arial 15 bold',
                  command=mat.mostrar)
botao.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
