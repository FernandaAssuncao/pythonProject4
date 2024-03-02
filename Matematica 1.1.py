from valida import leiaint
from random import choice, randint
from time import sleep
from math import sqrt


class Matematica:
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

    def __init__(self, bichinho):
        self.numero = None
        self.divisores = []
        self.raiz_quadrada = None
        self.par = None
        self.primo = None
        self.bichinhoo = bichinho

    def mudar_numero(self):
        if len(self.divisores) != 0:
            self.divisores.clear()
        self.numero = leiaint('Digite um número: ')
        self.__quais_divisores()
        self.__primo_ou_nao_primo()
        self.__par_ou_impar()
        self.__raiz_quadrada()
        print('\033[1:32mNúmero alterado com sucesso\033[m')

    def espera(self):
        self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}Aguarde analisando o número....\033[m')
        sleep(4)

    def __quais_divisores(self):
        for c in range(self.numero, 0, -1):
            if self.numero % c == 0:
                self.divisores.append(c)

    def mostrar_divisores(self):
        print(f'Os divisores de {self.numero} são ', end='')
        for c in self.divisores:
            print(f'{self.cores()}{c}\033[m, ', end='')
        print()

    def __raiz_quadrada(self):
        self.raiz_quadrada = sqrt(self.numero)

    def __primo_ou_nao_primo(self):
        if len(self.divisores) == 2:
            self.primo = 'É PRIMO'
        else:
            self.primo = 'NÃO É PRIMO'

    def __par_ou_impar(self):
        if 2 in self.divisores:
            self.par = 'PAR'
        else:
            self.par = 'IMPAR'

    def mostrar_par_impar(self):
        print(f'O número \033[1:33m{self.numero}\033[m é {self.cores()}{self.par}\033[m')

    def mostrar_primo_ou_nao_primo(self):
        print(f'O número \033[1:34m{self.numero}\033[m {self.cores()}{self.primo}\033[m')

    def mostrar_raiz_quadrada(self):
        print(f'A raiz quadrada de {self.numero} é {self.cores()}{self.raiz_quadrada:.1f}\033[m')


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
            print(f'{lista_cores[c]}[{c}] ✿\033[m')
        verdade = False
        escolha = None
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                escolha = lista_cores[opcao]
                verdade = True
            except:
                print('\033[1:31mErro,digite uma opção valida\033[m')
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
            print('\033[1:31mErro,bichinho não disponivel')

    def mostrar_bichinho(self):
        print(f'{self.cor}{self.bichinho}\033[m')

    def sortear_bichinho(self):
        return self.bichinhos_disponiveis[randint(0, 6)]

    def mudar_cor_do_bichinho(self):
        self.cor = self.nova_cor()


bicho = Bichinho()
mat = Matematica(bichinho=bicho)
while True:
    print('''\033[1:35:40m  Menu  \033[m
    \033[1:30m[1] mudar número
    [2] divisores
    [3] raiz quadrada
    [4] par ou impar
    [5] primo ou não primo
    [6] mudar cor bichinho
    [7] sair\033[m''')
    opcaoo = leiaint('Sua opção: ')
    if opcaoo == 1:
        mat.mudar_numero()
        mat.espera()
        print('-' * 70)
    elif opcaoo == 2:
        mat.mostrar_divisores()
        print('-' * 70)
    elif opcaoo == 3:
        mat.mostrar_raiz_quadrada()
        print('-' * 70)
    elif opcaoo == 4:
        mat.mostrar_par_impar()
        print('-' * 70)
    elif opcaoo == 5:
        mat.mostrar_primo_ou_nao_primo()
        print('-' * 70)
    elif opcaoo == 6:
        mat.bichinhoo.mudar_cor_do_bichinho()
        print('-' * 70)
    elif opcaoo == 7:
        print('-' * 70)
        break
    else:
        print('\033[1:31mErro,por favor digite uma opção valída\033[m')
        print('-' * 70)
