from tkinter import ttk
from random import randint, choice
import tkinter as tk


class JogoAdivinhacaoNumero:
    @staticmethod
    def __mudar_numeros_disponiveis(num):
        lista = []
        for c in range(1, num + 1):
            lista.append(c)
        return lista

    @staticmethod
    def mensagens():
        lista = ['Errou feio em kkkkk',
                 'Eita....',
                 'Santa Burrice',
                 'Meu deus que burro(a)',
                 'Se liga em',
                 'Tá fumando maconha']
        return choice(lista)

    def __init__(self):
        self.nivel = 'facíl'
        self.numero_sorteado = None
        self.numero_nivel = 50
        self.usuario = None
        self.tentativas = 0
        self.numeros_disponiveis = []
        self.novos_numeros()

    def novos_numeros(self):
        self.numeros_disponiveis = self.__mudar_numeros_disponiveis(num=self.numero_nivel)

    def mudar_nivel(self):
        self.nivel = niveis.get()
        self.nivel = str(self.nivel)
        if self.nivel == 'facíl':
            self.numero_nivel = 50
        elif self.nivel == 'medío':
            self.numero_nivel = 150
        elif self.nivel == 'difícil':
            self.numero_nivel = 500
        aviso['text'] = 'Nivel alterado com sucesso'
        self.novos_numeros()
        mensagem1['text'] = f'Escolha um número entre 1 e {self.numero_nivel}'

    def sortear_numero(self):
        self.zerar_tentativas()
        self.numero_sorteado = randint(1, self.numero_nivel)
        aviso1['text'] = 'Tente acertar, quero ver \nvocê conseguir'

    def mudar_tentativas(self):
        self.tentativas += 1
        tentativas_['text'] = f'Tentativas: {self.tentativas}'

    def zerar_tentativas(self):
        self.tentativas = 0
        tentativas_['text'] = f'Tentativas: {self.tentativas}'

    def jogar(self):
        try:
            self.usuario = numero.get()
            self.usuario = int(self.usuario)
            self.mudar_tentativas()
            if self.usuario == self.numero_sorteado:
                partida['fg'] = 'white'
                partida['text'] = f'Parabens você acertou!\nO número sorteado foi {self.numero_sorteado}'
            else:
                if self.usuario > self.numero_sorteado:
                    partida['fg'] = 'white'
                    partida['text'] = f'{self.mensagens()}.\nNúmero muito alto'
                elif self.usuario < self.numero_sorteado:
                    partida['fg'] = 'white'
                    partida['text'] = f'{self.mensagens()}.\nNúmero muito baixo'
        except:
            partida['fg'] = 'red'
            partida['text'] = 'Erro,faça tudo \nque se pede acima!'


jogo = JogoAdivinhacaoNumero()
janela = tk.Tk()
janela.title('')
janela.configure(bg='black')


# Titulo da Pagina
titulo = tk.Label(text='Jogo \n da adivinhação', borderwidth=4, relief='ridge', bg='#FFB6C1', fg='black',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

# Mudar niveis

mensagem = tk.Label(text='Mude o nivel de diiculdade aqui', bg='black', fg='white', font='Arial 9 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

tentativas_ = tk.Label(text='Tentativas: 0', borderwidth=4, bg='#FA8072', fg='black', font='Arial 9 bold',
                       relief='ridge')
tentativas_.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

niveis = tk.StringVar(value='facíl')

botao_nivelfacil = tk.Radiobutton(text='Nivel Facíl', variable=niveis, value='facíl', command=jogo.mudar_nivel,
                                  bg='black', fg='#F08080', font='Arial 8 bold')
botao_nivelfacil.grid(row=2, column=0, padx=10, pady=10, sticky='nswe')

botao_nivelmedio = tk.Radiobutton(text='Nivel Medío', variable=niveis, value='medío', command=jogo.mudar_nivel,
                                  bg='black', fg='#F08080', font='Arial 8 bold')
botao_nivelmedio.grid(row=2, column=1, padx=10, pady=10, sticky='nswe')

botao_niveldificil = tk.Radiobutton(text='Nivel difícil', variable=niveis, value='difícil', command=jogo.mudar_nivel,
                                    bg='black', fg='#F08080', font='Arial 8 bold')
botao_niveldificil.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFC0CB', fg='black', font='Arial 9 bold')
aviso.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

aviso1 = tk.Label(text='', bg='black', fg='white', font='Arial 9 bold')
aviso1.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_sortear_numero = tk.Button(text='Sortear Número', bg='#F08080', fg='black', font='Arial 9 bold',
                                 command=jogo.sortear_numero)
botao_sortear_numero.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

mensagem1 = tk.Label(text='Escolha um número entre 1 e 50', bg='black', fg='#F08080', font='Arial 9 bold')
mensagem1.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

numero = ttk.Combobox(values=jogo.numeros_disponiveis)
numero.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

partida = tk.Label(text='', bg='black', fg='white', font='Arial 9 bold')
partida.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_jogar = tk.Button(text='Jogar', bg='#F08080', fg='black', font='Arial 9 bold', command=jogo.jogar)
botao_jogar.grid(row=6, column=2, padx=10, pady=10, sticky='nswe')

botao_fechar_jogo = tk.Button(text='Fechar Jogo', bg='#F08080', fg='black', font='Arial 9 bold',
                              command=janela.quit)
botao_fechar_jogo.grid(row=7, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
