from random import randint, choice
from tkinter import ttk
import tkinter as tk


class Simulador_de_dado:
    @staticmethod
    def cores():
        lista = ['pink',
                'white',
                'green',
                'red',
                'yellow',
                'purple']
        return choice(lista)

    def __init__(self, bichinho):
        self.dado = None
        self.bichinhoo = bichinho


    def girar_dado(self):
        self.dado = randint(1, 6)
        dado['foreground'] = self.cores()
        dado['background'] = 'black'
        self.niveis_bichinho()
        bichino['text'] = f'{self.bichinhoo.bichinho}'
        bichino['foreground'] = self.bichinhoo.cor
        dado['text'] = f'    O número que caiu......{self.dado}   '

    def niveis_bichinho(self):
        if (self.dado > 5) and (self.dado <= 6):
            self.bichinhoo.mudar_bichinho(novo='(\_/)\n(0_0)\nC(")(")')
        elif (self.dado > 3) and (self.dado <= 4):
            self.bichinhoo.mudar_bichinho(novo='{\_/}\n(•-•)\n > < ')
        else:
            self.bichinhoo.mudar_bichinho(novo='(\_/)\n(X.X)\n(") (")|')


class Bichinho:
    @staticmethod
    def cores_bichinhos():
        lista = ['red',
                 'purple',
                 'green']
        return choice(lista)

    def __init__(self):
        self.bichinho = '(\_/)\n(0_0)\nC(")(")'
        self.cor = 'green'
        self.cores_bichinhoss = ['red',
                                'purple',
                                'green']
        self.bichinhos_disponiveis = ['(\_/)\n(0_0)\nC(")(")',
                                      ' /)/)\n(^.^)\nC(")(")',
                                      '(\_/)\n(X.X)\n(") (")|',
                                      '(\ /)\n(* *)\nC(")(")',
                                      '( Y )\n( 0 0)\no(")(")',
                                      '{\_/}\n(•-•)\n > < ',
                                      '{\_/}\n(•.•)\n/ ^ ^']

    def mudar_bichinho(self, novo):
        if novo in self.bichinhos_disponiveis:
            self.bichinho = novo
        else:
            print('\033[1:31mBichinho não disponiel\033[m')

    def sortear_bichinho(self):
        return choice(self.bichinhos_disponiveis)

    def mudar_cor(self):
        self.cor = cores.get()
        mensagem['foreground'] = 'green'
        mensagem['text'] = 'Cor alterada com sucesso'


janela = tk.Tk()
bicho = Bichinho()
simulador = Simulador_de_dado(bichinho=bicho)

janela.title('Simulador de dado')

titulo = tk.Label(text='Simulador de dado', borderwidth=2, relief='solid')
titulo.grid(row=0, column=0, columnspan=3, sticky='nswe', padx=10, pady=10)

bichino = tk.Label(text='')
bichino.grid(row=1, column=0, padx=10, pady=10, columnspan=1, sticky='nswe')

dado = tk.Label(text='', anchor='e')
dado.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky='nswe')

botao_dado = tk.Button(text='Girar dado', command=simulador.girar_dado)
botao_dado.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Mudar cor bichinho', borderwidth=2, relief='solid')
titulo2.grid(row=3, column=0, padx=10, pady=10, columnspan=3, sticky='nswe')

cores = ttk.Combobox(values=simulador.bichinhoo.cores_bichinhoss)
cores.grid(row=4, column=0, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='')
mensagem.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_cor = tk.Button(text='Mudar cor', command=simulador.bichinhoo.mudar_cor)
botao_mudar_cor.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar', command=janela.quit, fg='red')
botao_fechar.grid(row=6, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
