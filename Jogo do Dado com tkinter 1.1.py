from random import randint
from tkinter import ttk
import tkinter as tk


class JogoDoDado:
    @staticmethod
    def __mudar_numeros(num):
        lista = []
        for c in range(1, num + 1):
            lista.append(c)
        return lista

    def __init__(self):
        self.dado = None
        self.vencedor = None
        self.aposta_usuario = None
        self.aposta_computador = None
        self.numeros_disponiveis = self.__mudar_numeros(num=6)

    def girar_dado(self):
        self.dado = randint(1, 6)
        mensagem_dado['text'] = f'Caiu {self.dado}\n no dado!'
        if self.aposta_usuario is not None:
            self.atualizar_vencedor()
            self.mostrar_vencedor()

    def atualizar_vencedor(self):
        if self.aposta_usuario == self.dado:
            self.vencedor = 'usuario'
        elif self.aposta_computador == self.dado:
            self.vencedor = 'computador'
        else:
            self.vencedor = 'nenhum'

    def mostrar_vencedor(self):
        vitoria['text'] = f'Vencedor: {self.vencedor}'

    def apostar(self):
        try:
            apostaa = aposta.get()
            apostaa = int(apostaa)
            if apostaa in self.numeros_disponiveis:
                self.aposta_usuario = apostaa
                self.aposta_computador = randint(1, 6)
                aviso['fg'] = 'black'
                aviso['text'] = 'Aposta Atualizada\n com sucesso!'
                aposta1['text'] = f'Sua Aposta: {self.aposta_usuario}'
                aposta2['text'] = f'Aposta Computador: {self.aposta_computador}'
            else:
                raise
        except:
            aviso['fg'] = 'red'
            aviso['text'] = 'Erro, digite\n o que se pede!'


jogo = JogoDoDado()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFF8DC')

titulo = tk.Label(text='Jogo do\n Dado', borderwidth=4, relief='ridge', bg='#FFE4B5', fg='black',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem_dado = tk.Label(text='', bg='#FFF8DC', fg='black', font='Arial 10 bold')
mensagem_dado.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_girar_dado = tk.Button(text='Girar Dado', bg='#FFE4B5', fg='black', font='Arial 12 bold',
                             command=jogo.girar_dado)
botao_girar_dado.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

titulo2 = tk.Label(text='O que você acha\n que vai cair?', borderwidth=4, relief='ridge',
                   bg='#FFE4B5', fg='black', font='Arial 15 bold')
titulo2.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Aposte aqui ->', bg='#FFF8DC', fg='black', font='Arial 10 bold')
mensagem.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

aposta = ttk.Combobox(values=jogo.numeros_disponiveis)
aposta.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

aviso = tk.Label(text='', bg='#FFF8DC', fg='black', font='Arial 10 bold')
aviso.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_apostar = tk.Button(text='Apostar', bg='#FFE4B5', fg='black', font='Arial 12 bold',
                          command=jogo.apostar)
botao_apostar.grid(row=4, column=2, padx=10, pady=10, sticky='nswe')

aposta1 = tk.Label(text='Sua aposta: ', borderwidth=4, relief='ridge', bg='#FFE4B5', fg='black',
                   font='Arial 12 bold')
aposta1.grid(row=5, column=0, columnspan=1, padx=10, pady=10, sticky='nswe')

aposta2 = tk.Label(text='Aposta computador: ', borderwidth=4, relief='ridge', bg='#FFE4B5', fg='black',
                   font='Arial 12 bold')
aposta2.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

vitoria = tk.Label(text='Vencedor: ', borderwidth=4, relief='raised', bg='#FFE4B5', fg='black',
                   font='Arial 12 bold')
vitoria.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text='Fechar Jogo', bg='#FFE4B5', fg='black', font='Arial 12 bold',
                         command=janela.quit)
botao_fechar.grid(row=6, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
