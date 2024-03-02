from random import randint
from tkinter import ttk
import tkinter as tk


class JogoDaAdivinhacao:
    @staticmethod
    def __adicionar_numeros_disponiveis():
        lista = []
        for c in range(1, 51):
            lista.append(c)
        return lista

    def __init__(self):
        self.numero_sorteado = None
        self.usuario = None
        self.tentativas = 10
        self.numeros_disponiveis = self.__adicionar_numeros_disponiveis()

    def reiniciar_tentativas(self):
        self.tentativas = 10

    def mostrar_tentativas(self):
        tentativas_restantes['text'] = f'Tentativas: {self.tentativas}'

    def sortear_numero(self):
        self.numero_sorteado = randint(1, 50)
        self.reiniciar_tentativas()
        self.mostrar_tentativas()

    def diminuir_tentativas(self):
        self.tentativas -= 1

    def analisar_escolha(self):
        self.diminuir_tentativas()
        self.mostrar_tentativas()
        if self.tentativas == 0 or self.tentativas < 0:
            self.tentativas = 0
            self.mostrar_tentativas()
            aviso['fg'] = 'red'
            aviso['text'] = 'Suas tentativas acabaram\nsortei o valor novamente para reiniciar.'
        else:
            if self.usuario == self.numero_sorteado:
                aviso['fg'] = 'white'
                aviso['text'] = f'Parabens você\nO número sorteado foi {self.numero_sorteado}\nJogo já iniciado novamente'
                self.sortear_numero()
            else:
                if self.usuario > self.numero_sorteado:
                    aviso['fg'] = 'white'
                    aviso['text'] = 'Você errou,\n valor muito alto!'
                elif self.usuario < self.numero_sorteado:
                    aviso['fg'] = 'white'
                    aviso['text'] = 'Você errou,\n valor muito baixo!'

    def jogar(self):
        try:
            num = escolha.get()
            num = int(num)
            if num in self.numeros_disponiveis and self.numero_sorteado is not None:
                self.usuario = num
                self.analisar_escolha()
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Faça o que se pede\n acima pra continuar.'


jogo = JogoDaAdivinhacao()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#DDA0DD')

titulo = tk.Label(text='Jogo da\n Adivinhacao', borderwidth=6, relief='ridge', bg='#EE82EE', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

tentativas_restantes = tk.Label(text=f'Tentativas: {jogo.tentativas}', borderwidth=4, relief='ridge', bg='#EE82EE',
                                fg='white', font='Arial 12 bold')
tentativas_restantes.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_sortear_valor = tk.Button(text='Sortear Número', bg='#EE82EE', fg='white', font='Arial 12 bold',
                                command=jogo.sortear_numero)
botao_sortear_valor.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Aposte um valor aqui', bg='#DDA0DD', fg='white', font='Arial 10 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=jogo.numeros_disponiveis)
escolha.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#DDA0DD', fg='white', font='Arial 12 bold')
aviso.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_jogar = tk.Button(text='Jogar', bg='#EE82EE', fg='white', font='Arial 12 bold',
                        command=jogo.jogar)
botao_jogar.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
