from tkinter import ttk
from random import choice
import tkinter as tk


class Jokenpo:
    def __init__(self):
        self.__pontos_usuario = 0
        self.__pontos_computador = 0
        self.usuario = None
        self.computador = None
        self.vencedor = None
        self.escolhas_disponiveis = ['pedra', 'papel', 'tesoura']

    def __mudar_computador(self):
        return choice(self.escolhas_disponiveis)

    def veficar_vencedor(self):
        if (self.usuario == 'pedra') and (self.computador == 'pedra'):
            self.vencedor = 'empate'
        elif (self.usuario == 'pedra') and (self.computador == 'papel'):
            self.vencedor = 'computador'
        elif (self.usuario == 'pedra') and (self.computador == 'tesoura'):
            self.vencedor = 'usuario'
        elif (self.usuario == 'papel') and (self.computador == 'pedra'):
            self.vencedor = 'usuario'
        elif (self.usuario == 'papel') and (self.computador == 'papel'):
            self.vencedor = 'empate'
        elif (self.usuario == 'papel') and (self.computador == 'tesoura'):
            self.vencedor = 'computador'
        elif (self.usuario == 'tesoura') and (self.computador == 'pedra'):
            self.vencedor = 'computador'
        elif (self.usuario == 'tesoura') and (self.computador == 'papel'):
            self.vencedor = 'usuario'
        elif (self.usuario == 'tesoura') and (self.computador == 'tesoura'):
            self.vencedor = 'empate'

    def mostrar_resultados(self):
        resultado_jogo['fg'] = 'black'
        resultado_jogo['text'] = f'Você escolheu {self.usuario}\nComputador escolheu {self.computador}\nVencedor: {self.vencedor}'

    def atualizar_pontos(self):
        if self.vencedor == 'usuario':
            self.__pontos_usuario += 1
        elif self.vencedor == 'computador':
            self.__pontos_computador += 1
        elif self.vencedor == 'empate':
            pass

    def atualizar_informacoes(self):
        placar['text'] = f'{self.__pontos_usuario} X {self.__pontos_computador}'

    def mudar_usuario(self):
        try:
            usuario = escolha.get()
            if usuario in self.escolhas_disponiveis:
                self.usuario = usuario
                self.computador = self.__mudar_computador()
                self.veficar_vencedor()
                self.mostrar_resultados()
                self.atualizar_pontos()
                self.atualizar_informacoes()
            else:
                raise
        except:
            resultado_jogo['fg'] = 'red'
            resultado_jogo['text'] = 'Erro,opção invalida'


jogo = Jokenpo()
janela = tk.Tk()
janela.title('')
janela.configure(bg='#B0E0E6')

titulo = tk.Label(text='Jokenpo', borderwidth=6, relief='ridge', bg='#40E0D0', fg='white', font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

placar = tk.Label(text='0 X 0', bg='#B0E0E6', fg='white', font='Arial 35 bold')
placar.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='Pedra,papel ou tesoura?', bg='#B0E0E6', fg='white', font='Arial 8 bold')
mensagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

escolha = ttk.Combobox(values=jogo.escolhas_disponiveis)
escolha.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

resultado_jogo = tk.Label(text='', bg='#B0E0E6', font='Arial 8 bold')
resultado_jogo.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_mudar_escolha = tk.Button(text='Jogar', bg='#40E0D0', fg='white', font='Arial 15 bold',
                                command=jogo.mudar_usuario)
botao_mudar_escolha.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
