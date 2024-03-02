from valida import leiaint
from math import sqrt
from random import choice, randint
from time import sleep
from datetime import datetime
from pytz import timezone


class Matematica:
    @staticmethod
    def div(numero):
        lista = []
        for c in range(numero, 0, -1):
            if numero % c == 0:
                lista.append(c)
        return lista

    @staticmethod
    def cores():
        lista = ['\033[1:31m',
                 '\033[1:32m',
                 '\033[1:33m',
                 '\033[1:34m',
                 '\033[1:35m',
                 '\033[1:36m']
        return choice(lista)

    @staticmethod
    def data_hora():
        fuso_br = timezone('brazil/East')
        horario = datetime.now(fuso_br)
        return horario.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, bichinho):
        self.numero = None
        self.historico = []
        self.divisores = []
        self.bichinhoo = bichinho

    def espera(self):
        self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.bichinho_disponiveis[randint(0, 6)])
        print(f'\033[1:37m{self.bichinhoo.bichinho} Analisando o número aguarde...', end='')
        sleep(4)
        print('terminei\033[m')

    def mudar_numero(self):
        self.numero = leiaint('Digite um número INTEIRO: ')
        self.historico.append((self.numero,
                               self.data_hora()))
        print('\033[1:32mNúmero alterado com sucesso!!\033[m')
        if len(self.divisores) != 0:
            self.divisores.clear()
        self.divisores = self.div(numero=self.numero)

    def raiz_quadrada(self):
        raiz = sqrt(self.numero)
        self.bichinhoo.mudar_bichinho(novo='(\ /)\n(* *)\nC(")(")')
        print(f'{self.bichinhoo.bichinho} A raiz de {self.cores()}{self.numero}\033[m é {self.cores()}{raiz:.1f}\033[m!!')

    def mostrar_divisores(self):
        self.bichinhoo.mudar_bichinho(novo='(\_/)\n(0_0)\nC(")(")')
        print(f'{self.bichinhoo.bichinho} Os divisores de \033[1:37m{self.numero}\033[m são ', end='')
        for c in range(0, len(self.divisores)):
            print(f'{self.cores()}{self.divisores[c]}\033[m, ', end='')
        print()

    def primo_ou_nao_primo(self):
        self.bichinhoo.mudar_bichinho(novo='{\_/}\n(•-•)\n > < ')
        if len(self.divisores) == 2:
            print(f'{self.bichinhoo.bichinho} O número {self.cores()}{self.numero} \033[1:32mé primo!!\033[m')
        else:
            print(f'{self.bichinhoo.bichinho} O número {self.cores()}{self.numero} \033[1:31mnão é primo!!\033[m')

    def par_ou_impar(self):
        self.bichinhoo.mudar_bichinho(novo='(\_/)\n(X.X)\n(") (")|')
        if 2 in self.divisores:
            print(f'{self.bichinhoo.bichinho} O número {self.cores()}{self.numero}\033[m é \033[1:32mPar!\033[m')
        else:
            print(f'{self.bichinhoo.bichinho} O número {self.cores()}{self.numero}\033[m é \033[1:31mImpar\033[m')

    def mostrar_historico(self):
        print('=================== Historico ==================')
        for n, dh in self.historico:
            print(f'Número {self.cores()}{n}\033[m pesquisado ás {self.cores()}{dh}\033[m')


class Bichinho:
    def __init__(self):
        self.bichinho = '(\_/)\n(0_0)\nC(")(")'
        self.bichinho_disponiveis = ['(\_/)\n(0_0)\nC(")(")',
                                      ' /)/)\n(^.^)\nC(")(")',
                                      '(\_/)\n(X.X)\n(") (")|',
                                      '(\ /)\n(* *)\nC(")(")',
                                      '( Y )\n( 0 0)\no(")(")',
                                      '{\_/}\n(•-•)\n > < ',
                                      '{\_/}\n(•.•)\n/ ^ ^']

    def mudar_bichinho(self, novo):
        if novo in self.bichinho_disponiveis:
            self.bichinho = novo
        else:
            print('\033[1:31mErro,bichinho não disponivel\033[m')


bicho = Bichinho()
mat = Matematica(bichinho=bicho)
while True:
    print(f'''\033[1:34:40m  Menu  \033[m
    \033[1:30m[1] mudar número
    [2] raiz quadrada
    [3] divisores
    [4] primo ou não primo
    [5] par ou impar
    [6] historico de pesquisa
    [7] sair\033[m''')
    opcao = leiaint('Sua opção: ')
    if opcao == 1:
        mat.mudar_numero()
        mat.espera()
        print('-' * 65)
    elif opcao == 2:
        mat.raiz_quadrada()
        print('-' * 65)
    elif opcao == 3:
        mat.mostrar_divisores()
        print('-' * 65)
    elif opcao == 4:
        mat.primo_ou_nao_primo()
        print('-' * 65)
    elif opcao == 5:
        mat.par_ou_impar()
        print('-' * 65)
    elif opcao == 6:
        mat.mostrar_historico()
        print('-' * 65)
    elif opcao == 7:
        mat.bichinhoo.mudar_bichinho(novo=' /)/)\n(^.^)\nC(")(")')
        print('\033[1:30mSaindo....')
        sleep(5)
        print(f'{mat.cores()}{mat.bichinhoo.bichinho} Tchauzinho até a proxima\033[m')
        print('-' * 65)
        break
    else:
        print('\033[1:31mErro,opção invalida\033[m')
