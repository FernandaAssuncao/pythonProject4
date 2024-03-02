from random import randint, choice
from time import sleep
from valida import leiaint


class Gerador_de_matriz:
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
        self.bichinhoo = bichinho
        self.matrix = []

    def espera(self):
        self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}Aguarde gerando matriz.....\033[m')
        sleep(4)

    def gerar_matrix(self):
        linha = []
        for c in range(0, 3):
            for i in range(0, 3):
                linha.append(randint(1, 9))
            self.matrix.append(linha[:])
            linha.clear()

    def mostrar_matrix(self):
        print('-' * 10)
        for linha in self.matrix:
            for numero in linha:
                print(f'{self.cores()}{numero}\033[m ', end='')
            print()
        print('-' * 10)

    def deletar_matriz(self):
        self.matrix.clear()


class Bichinho:
    @staticmethod
    def nova_cor():
        lista = ['\033[1:30m',
                 '\033[1:31m',
                 '\033[1:32m',
                 '\033[1:33m',
                 '\033[1:34m',
                 '\033[1:35m',
                 '\033[1:36m',
                 '\033[1:37m']
        for c in range(0, len(lista)):
            print(f'{lista[c]}[{c}] ⛵\033[m')
        verdade = False
        escolha = ''
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                escolha = lista[opcao]
                verdade = True
            except:
                print('\033[1:31mOpção invalida\033[m')
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
            print('\033[1:31mBichinho não disponivel\033[m')

    def mostrar_bichinho(self):
        print(f'{self.cor}{self.bichinho}\033[m')

    def sortear_bichinho(self):
        return choice(self.bichinhos_disponiveis)

    def mudar_cor(self):
        self.cor = self.nova_cor()


bicho = Bichinho()
gerador = Gerador_de_matriz(bichinho=bicho)
while True:
    print('''\033[1:34:40m  Menu de opções  \033[m
    \033[1:30m[1] mudar cor do bichinho
    [2] gerar matriz
    [3] sair\033[m''')
    opcaoo = leiaint('Digite sua opção: ')
    if opcaoo == 1:
        gerador.bichinhoo.mudar_cor()
        print('=' * 65)
    elif opcaoo == 2:
        gerador.espera()
        gerador.gerar_matrix()
        gerador.mostrar_matrix()
        gerador.deletar_matriz()
        print('=' * 65)
    elif opcaoo == 3:
        print('=' * 65)
        break
