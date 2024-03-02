from valida import leiaint
from random import choice
from datetime import datetime
from time import sleep
from pytz import timezone


class Tabuadas:
    @staticmethod
    def cores():
        lista = ['\033[1:30m',
                 '\033[1:31m',
                 '\033[1:32m',
                 '\033[1:33m',
                 '\033[1:34m',
                 '\033[1:35m',
                 '\033[1:36m',
                 '\033[1:37m']
        return choice(lista)

    @staticmethod
    def __data_e_hora():
        fuso_br = timezone('brazil/East')
        horario = datetime.now(fuso_br)
        return horario.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, bichinho):
        self.numero = None
        self.tabuada = []
        self.historico = []
        self.bichinhoo = bichinho

    def mudar_numero(self):
        if len(self.tabuada) != 0:
            self.apagar_tabuada_anterior()
        self.numero = leiaint('Digite um número para saber a sua tabuada: ')
        self.adicionar_ao_historico()
        self.espera()
        self.__criar_tabuada()

    def espera(self):
        self.bichinhoo.mudar_bichinho(self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}Aguarde analisando número.....\033[m')
        sleep(4)

    def __criar_tabuada(self):
        for c in range(1, 11):
            self.tabuada.append(self.numero * c)

    def mostrar_tabuada(self):
        print(f'\033[1:31:40m   Tabuada do {self.numero}   \033[m')
        for c in range(1, 11):
            print(f'\033[1:34m{self.numero}\033[m X \033[1:35m{c}\033[m = \033[1:32m{self.tabuada[c - 1]}\033[m')

    def adicionar_ao_historico(self):
        self.historico.append((self.numero,
                               self.__data_e_hora()))

    def apagar_tabuada_anterior(self):
        self.tabuada.clear()

    def mostrar_historico(self):
        print('\033[1:30:45m         Historico        \033[m')
        for n, dh in self.historico:
            print(f'Número {n} pesquisado {dh}')


class Bichinho:
    @staticmethod
    def __nova_cor():
        lista_cores = ['\033[1:30m',
                       '\033[1:31m',
                       '\033[1:32m',
                       '\033[1:33m',
                       '\033[1:34m',
                       '\033[1:35m',
                       '\033[1:36m',
                       '\033[1:37m']
        print('\033[1:35:40m    Menu escolhas   \033[m')
        for c in range(0, len(lista_cores)):
            print(f'{lista_cores[c]}[{c}] X\033[m')
        verdade = False
        escolha = None
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                escolha = lista_cores[opcao]
                verdade = True
            except:
                print('\033[1:31mErro,opção invalida\033[m')
            if verdade is True:
                return escolha

    def __init__(self):
        self.bichinho = '(\_/)\n(0_0)\nC(")(")'
        self.cor = '\033[1:37m'
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
            print('\033[1:31mErro,bichinho não disponivel\033[m')

    def sortear_bichinho(self):
        return choice(self.bichinhos_disponiveis)

    def mostrar_bichinho(self):
        print(f'{self.cor}{self.bichinho}\033[m')

    def mudar_cor(self):
        self.cor = self.__nova_cor()


bicho = Bichinho()
tabu = Tabuadas(bichinho=bicho)
while True:
    print('''\033[1:32:40m   MENU \033[m
    \033[1:30m[1] Mudar cor do bichinho 
    [2] Mudar número
    [3] Ver tabuada
    [4] Ver historico
    [5] Sair\033[m''')
    opcoes = leiaint('Sua opção: ')
    if opcoes == 1:
        tabu.bichinhoo.mudar_cor()
        print('-' * 65)
    elif opcoes == 2:
        tabu.mudar_numero()
        print('-' * 65)
    elif opcoes == 3:
        tabu.mostrar_tabuada()
        print('-' * 65)
    elif opcoes == 4:
        tabu.mostrar_historico()
        print('-' * 65)
    elif opcoes == 5:
        print('-' * 65)
        break
