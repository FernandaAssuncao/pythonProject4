from random import randint, choice
from tkinter import ttk
import tkinter as tk


class JogoDoDado:
    @staticmethod
    def mensagens():
        lista = ['Nossa muito dificil',
                 'Facíl d+',
                 'Se errar é burro(a)',
                 'iii muito dificil',
                 'Você não vai acertar kkkkkkkkk']
        return choice(lista)

    @staticmethod
    def mensagens_de_erro():
        lista = ['Sabia que não ia acertar',
                 'Muito Burro',
                 'Nossa errou feio em',
                 'Meu Deus kkkkkkkkk',
                 'Sem comentarios....']
        return choice(lista)

    def __init__(self):
        self.dado = None
        self.chute = None
        self.tentativas = 5
        self.numeros_disponiveis = [c for c in range(1, 7)]

    def girar_dado(self):
        self.tentativas = 5
        self.dado = randint(1, 6)
        mensagem_dado['text'] = f'{self.mensagens()}'

    def jogar(self):
        try:
            num = chute.get()
            num = int(num)
            if num in self.numeros_disponiveis and self.dado is not None:
                self.chute = num
                self.tentativas = self.tentativas - 1
                tentativass['text'] = f'Tentativas restantes: {self.tentativas}'
                if self.chute == self.dado:
                    aviso['fg'] = 'white'
                    aviso['text'] = f'Parabens você acertou\nO número que caiu no dado foi {self.dado}'
                    self.tentativas = 5
                elif self.tentativas == 0:
                    aviso['fg'] = 'white'
                    aviso['text'] = f'Suas tentativas acabarem\ngire o dado novamente\npara reinicialas\nO número que caiu foi {self.dado}'
                else:
                    aviso['fg'] = 'white'
                    aviso['text'] = f'{self.mensagens_de_erro()}'
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro,algo deu errado!'


jogo = JogoDoDado()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#E0FFFF')

titulo = tk.Label(text='Jogo do Dado', borderwidth=4, relief='raised', bg='#ADD8E6', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

tentativass = tk.Label(text='Tentativas restantes: 5', bg='#ADD8E6', fg='white', font='Arial 10 bold')
tentativass.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

mensagem_dado = tk.Label(text='Clique para girar o dado', bg='#E0FFFF', fg='#87CEEB', font='Arial 8 bold')
mensagem_dado.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_girar_dado = tk.Button(text='Girar Dado', bg='#ADD8E6', fg='white', font='Arial 12 bold',
                             command=jogo.girar_dado)
botao_girar_dado.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

titulo1 = tk.Label(text='Jogar', borderwidth=4, relief='raised', bg='#ADD8E6', fg='white',
                   font='Arial 12 bold')
titulo1.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Tente acertar o número\n que caiu no dado', bg='#E0FFFF', fg='#87CEEB',
                    font='Arial 8 bold')
mensagem.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

chute = ttk.Combobox(values=jogo.numeros_disponiveis)
chute.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#ADD8E6', fg='white', font='Arial 8 bold')
aviso.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_jogar = tk.Button(text='Jogar', bg='#ADD8E6', fg='white', font='Arial 12 bold',
                        command=jogo.jogar)
botao_jogar.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
