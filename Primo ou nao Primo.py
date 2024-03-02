from valida import leiaint
from random import choice


class PrimoOuNaoPrimo:
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
        self.bichinhoo = bichinho

    def mudar_numero(self):
        if len(self.divisores) != 0:
            self.divisores.clear()
        self.numero = leiaint('Digite um número INTEIRO: ')
        print('\033[1:32mNúmero alterado com sucesso!\033[m')
        self.__quais_divisores()

    def __quais_divisores(self):
        for c in range(self.numero, 0, -1):
            if self.numero % c == 0:
                self.divisores.append(c)

    def mostrar_divisores(self):
        print(f'Os divisores de {self.cores()}{self.numero}\033[m são ', end='')
        for num in self.divisores:
            print(f'{self.cores()}{num}\033[m, ', end='')
        print()

    def primo_ou_nao_primo(self):
        if len(self.divisores) == 2:
            print(f'O {self.cores()}{self.numero}\033[m \033[1:32mÉ\033[m PRIMO!')
        else:
            print(f'O {self.cores()}{self.numero}\033[m \033[1:31mNÃO É\033[m PRIMO!')


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
        print('\033[1:32:40m   Menu de cores   \033[m')
        for c in range(0, len(lista_cores)):
            print(f'{lista_cores[c]}[{c}] ☂\033[m')
        verdade = False
        escolha = ''
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                escolha = lista_cores[opcao]
                verdade = True
            except:
                print('\033[1:31mOpção não disponivel\033[m')
            if verdade:
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
            print('\033[1:31mBichinho não disponivel\033[m')

    def mudar_cor(self):
        self.cor = self.nova_cor()

    def mostrar_bichinho(self):
        print(f'{self.cor}{self.bichinho}\033[m')


bicho = Bichinho()
p = PrimoOuNaoPrimo(bichinho=bicho)

while True:
    print('''\033[1:31:40m   Menu   \033[m
    \033[1:30m[1] mudar número
    [2] ver divisores
    [3] primo ou não primo
    [4] sair\033[m''')
    opcaoo = leiaint('Sua opção: ')
    if opcaoo == 1:
        p.mudar_numero()
        print('-' * 75)
    elif opcaoo == 2:
        p.mostrar_divisores()
        print('-' * 75)
    elif opcaoo == 3:
        p.primo_ou_nao_primo()
        print('-' * 75)
    elif opcaoo == 4:
        print('-' * 75)
        break
    else:
        print('\033[1:31mOpção invalida\033[m')
        print('-' * 75)
