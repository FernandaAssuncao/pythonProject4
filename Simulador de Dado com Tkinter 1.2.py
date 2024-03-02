from random import randint
import tkinter as tk


class SimuladorDeDado:
    @staticmethod
    def __disponiveis_dado():
        lista = []
        for c in range(1, 7):
            lista.append(c)
        return lista

    def __init__(self):
        self.dado = None
        self.lista = [[0, 1],
                      [0, 2],
                      [0, 3],
                      [0, 4],
                      [0, 5],
                      [0, 6]]

    def girar_dado(self):
        self.dado = randint(1, 6)
        mensagem_dado['text'] = f'Caiu no dado......{self.dado}'
        self.mudar_ranking()
        self.mostrar_dois_primeiros()

    def mudar_ranking(self):
        lista_nova = []
        for quantidade, numero in self.lista:
            if self.dado == numero:
                quantidade += 1
            liste = [quantidade, numero]
            lista_nova.append(liste[:])
            liste.clear()
            self.lista = lista_nova
        self.lista.sort(reverse=True)

    def pegar_dois_primeiros(self):
        dois = []
        for c in range(0, 2):
            dois.append(self.lista[c])
        return dois

    def mostrar_dois_primeiros(self):
        lista = self.pegar_dois_primeiros()
        print(lista)
        n1['text'] = f'1º número {lista[0][1]}'
        n2['text'] = f'2º número {lista[1][1]}'


simulador = SimuladorDeDado()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFE4E1')

titulo = tk.Label(text='Simulador de Dado', borderwidth=4, relief='raised', bg='#FFB6C1', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem_dado = tk.Label(text='', bg='#FFE4E1', fg='#FFB6C1', font='Arial 10 bold')
mensagem_dado.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_girar_dado = tk.Button(text='Girar Dado', bg='#FFB6C1', fg='white', font='Arial 12 bold',
                             command=simulador.girar_dado)
botao_girar_dado.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Top 2 números que\n mais cairam no dado', borderwidth=4, relief='raised', bg='#FFB6C1',
                   fg='white', font='Arial 15 bold')
titulo2.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

n1 = tk.Label(text='1º ', bg='white', fg='#FFB6C1', font='Arial 10 bold')
n1.grid(row=3, column=1, padx=10, pady=10, sticky='nswe')

n2 = tk.Label(text='2º ', bg='white', fg='#FFB6C1', font='Arial 10 bold')
n2.grid(row=4, column=1, padx=10, pady=10, sticky='nswe')

janela.mainloop()
