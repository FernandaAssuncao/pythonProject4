from tkinter import ttk
from random import randint, choice
import tkinter as tk


class JogoDado:
    @staticmethod
    def mensagens():
        lista = ['Hummmm,tá difícil em',
                 'Eeee,até que tá facíl',
                 'Complicado em',
                 'kkkkkkk quero ver acertar',
                 'Não vai acertar nunca kkkkkkkk']
        return choice(lista)

    @staticmethod
    def mensagens_erro():
        lista = ['Errou,feio em',
                 'Nossa que burro',
                 'Nossa kkkkkkkkk',
                 'MEU DEUS kkkkkkkkkkk',
                 'Santa burrice em']
        return choice(lista)

    @staticmethod
    def cores():
        lista = ['#4B0082',
                 '#C71585',
                 '#4B0082',
                 '#7B68EE',
                 '#3CB371',
                 '#FF6347',
                 '#00FFFF',
                 '#1E90FF']
        return choice(lista)

    def __init__(self):
        self.numero = None
        self.dado = None
        self.tentativas = 0
        self.numeros_disponiveis = [c for c in range(1, 7)]

    def girar_dado(self):
        self.dado = randint(1, 6)
        self.tentativas = 0
        mensagem_tentativas['text'] = 'Tentativas: 0'
        mensagem['fg'] = '#008B8B'
        mensagem['text'] = f'{self.mensagens()}'

    def mudar_numero_veficar_vencedor(self):
        try:
            num = escolha.get()
            self.numero = int(num)
            if self.numero in self.numeros_disponiveis:
                if self.numero == self.dado:
                    aviso['fg'] = f'{self.cores()}'
                    aviso['text'] = f'Parabens você acertou!\nO número que caiu no dado foi {self.dado}'
                else:
                    self.tentativas += 1
                    aviso['fg'] = f'{self.cores()}'
                    aviso['text'] = f'{self.mensagens_erro()}'
                    mensagem_tentativas['text'] = f'Tentavias: {self.tentativas}'
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Algo deu errado,\nfaça tudo que se pede acima'


janela = tk.Tk()
jogo = JogoDado()
janela.configure(bg='#FFB6C1')
janela.title('Jogo do dado')

titulo = tk.Label(text='Girar Dado', borderwidth=4, relief='ridge', bg='#FF69B4')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Clique aqui para girar o dado', bg='#FFB6C1')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_girar_dado = tk.Button(text='Girar Dado', bg='#FF1493', command=jogo.girar_dado)
botao_girar_dado.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

mensagem_tentativas = tk.Label(text='Tentativas: 0', borderwidth=2, relief='solid', bg='#FF69B4')
mensagem_tentativas.grid(row=2, column=0, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='Jogar', borderwidth=4, relief='ridge', bg='#FF69B4')
titulo2.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem2 = tk.Label(text='Escolha aqui entre 1 e 6', bg='#FFB6C1')
mensagem2.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=jogo.numeros_disponiveis)
escolha.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFB6C1')
aviso.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_jogar = tk.Button(text='Tentar', bg='#FF1493', command=jogo.mudar_numero_veficar_vencedor)
botao_jogar.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar Jogo', bg='#FF1493', command=janela.quit)
botao_fechar.grid(row=6, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
