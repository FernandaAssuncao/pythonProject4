from valida import leiaint
from time import sleep
from random import choice, randint
from datetime import datetime
from pytz import timezone


class Divisores:
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
    def data_e_hora():
        fuso_br = timezone('brazil/East')
        horario = datetime.now(fuso_br)
        return horario.strftime('%d/%M/%Y %H:%M:%S')

    def __init__(self, bichinho):
        self.numero = None
        self.divisores = []
        self.historico = []
        self.bichinhoo = bichinho

    def mudar_numero(self):
        if len(self.divisores) != 0:
            self.divisores.clear()
        self.numero = leiaint('Digite um número: ')
        self.__adicionar_ao_historico()
        print('\033[1:32mNúmero alterado com sucesso!\033[m')
        self.__divisores()

    def __divisores(self):
        for c in range(self.numero, 0, -1):
            if self.numero % c == 0:
                self.divisores.append(c)

    def mostrar_divisores(self):
        print(f'Os divisores de \033[1:30m{self.numero}\033[m são ', end='')
        for c in self.divisores:
            print(f'{self.cores()}{c}\033[m, ', end='')
        print()

    def espera(self):
        self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}Aguarde analisando número....\033[m')
        sleep(4)

    def mostrar_historico(self):
        print('================== \033[1:31:40m  Historico  \033[m ==================')
        for n, d in self.historico:
            print(f'{n:<15} {d}')
        print('-' * 55)

    def __adicionar_ao_historico(self):
        self.historico.append((self.numero,
                               self.data_e_hora()))


class Bichinho:
    @staticmethod
    def nova_cor():
        lista_cores = ['\033[1:30m',
                       '\033[1:31m',
                       '\033[1:32m',
                       '\033[1:33m',
                       '\033[1:34m',
                       '\033[1:35m',
                       '\033[1:36m',
                       '\033[1:37m']
        for c in range(0, len(lista_cores)):
            print(f'{lista_cores[c]}[{c}]  ⛄\033[m')
        verdade = False
        opcao = None
        while True:
            try:
                escolha = leiaint('Sua opção: ')
                opcao = lista_cores[escolha]
                verdade = True
            except:
                print('\033[1:31mErro,opção invalida\033[m')
            if verdade is True:
                print('\033[1:32mCor do bichinho alterada com sucesso!\033[m')
                return opcao

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
            print('\033[1:31mErro,bichinho não disponivel')

    def mostrar_bichinho(self):
        print(f'{self.cor}{self.bichinho}\033[m')

    def mudar_cor(self):
        self.cor = self.nova_cor()

    def sortear_bichinho(self):
        return self.bichinhos_disponiveis[randint(0, 6)]


bicho = Bichinho()
div = Divisores(bichinho=bicho)
while True:
    print('''\033[1:32:40m  Menu  \033[m
    \033[1:30m[1] mudar número
    [2] mostrar divisores
    [3] historico
    [4] mudar cor do bichinho
    [5] sair\033[m''')
    opcaoo = leiaint('Sua opção: ')
    if opcaoo == 1:
        div.mudar_numero()
        print('-' * 55)
    elif opcaoo == 2:
        div.espera()
        div.mostrar_divisores()
        print('-' * 55)
    elif opcaoo == 3:
        div.mostrar_historico()
    elif opcaoo == 4:
        div.bichinhoo.mudar_cor()
        print('-' * 55)
    elif opcaoo == 5:
        print('-' * 55)
        break
    else:
        print('\033[1:31mOpção invalida\033[m')
        print('-' * 55)
