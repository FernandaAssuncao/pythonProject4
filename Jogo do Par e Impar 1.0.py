from valida import leiaint
from random import randint, choice
from time import sleep


class JogoParImpar:
    @staticmethod
    def escolha():
        lista = ['par',
                 'impar']
        print('\033[1:34:40m  Menu de escolhas  \033[m')
        for c in range(0, len(lista)):
            print(f'\033[1:30m[{c}] {lista[c]}\033[m')
        verdade = False
        escolha = None
        while True:
            try:
                opcao = leiaint('Sua escolha? ')
                escolha = lista[opcao]
                verdade = True
            except:
                print('\033[1:31mOpção invalida,por favor digite uma valida\033[m')
            if verdade is True:
                return escolha

    @staticmethod
    def cores():
        lista_cores = ['\033[1:30m',
                       '\033[1:31m',
                       '\033[1:32m',
                       '\033[1:33m',
                       '\033[1:34m',
                       '\033[1:35m',
                       '\033[1:36m',
                       '\033[1:37m']
        return choice(lista_cores)

    def __init__(self, bichinho):
        self.escolha_usuario = None
        self.escolha_computador = None
        self.numero_usuario = None
        self.numero_computador = None
        self.soma = None
        self.bichinhoo = bichinho

    def espera(self):
        self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}Aguarde iniciando jogo...Boa sorte...\033[m')
        sleep(4)

    def mudar_escolha_usuario(self):
        self.escolha_usuario = self.escolha()
        if self.escolha_usuario == 'par':
            self.escolha_computador = 'impar'
        else:
            self.escolha_computador = 'par'

    def mostrar_escolhas(self):
        print(f'Você escolheu {self.cores()}{self.escolha_usuario}\033[m')
        print(f'E o computador ficou {self.cores()}{self.escolha_computador}\033[m')

    def sortear_valor_computador(self):
        self.numero_computador = randint(1, 10)

    def escolha_numero_usuario(self):
        self.numero_usuario = leiaint('Digite um número entre 1 e 10: ')

    def mostrar_numeros(self):
        print(f'Você escolheu o número {self.cores()}{self.numero_usuario}\033[m')
        print(f'O computador escolheu {self.cores()}{self.numero_computador}\033[m')

    def somar_numeros(self):
        self.soma = self.numero_usuario + self.numero_computador

    def mostrar_soma(self):
        print(f'A soma dos dois números foi {self.cores()}{self.soma}\033[m')

    def mostrar_vencedor(self):
        if self.escolha_usuario == 'par':
            if self.soma % 2 == 0:
                print('\033[1:32mVencedor: VOCÊ\033[m')
            else:
                print('\033[1:31mVencedor: Computador\033[m')
        elif self.escolha_usuario == 'impar':
            if self.soma % 2 == 0:
                print('\033[1:32mVencedor: Computador\033[m')
            else:
                print('\033[1:32mVencedor: VOCÊ\033[m')

    def apagar_soma(self):
        self.soma = 0

    def iniciar_jogo(self):
        self.apagar_soma()
        self.espera()
        self.mudar_escolha_usuario()
        self.mostrar_escolhas()
        print('-' * 65)
        self.sortear_valor_computador()
        self.escolha_numero_usuario()
        self.mostrar_numeros()
        self.somar_numeros()
        print('-' * 65)
        self.mostrar_soma()
        self.mostrar_vencedor()
        print('-' * 65)


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
            print(f'{lista_cores[c]}[{c}] ⚽\033[m')
        verdade = False
        escolha = None
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                escolha = lista_cores[opcao]
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
            print('\033[1:31mErro,bichinho não disponivel\033[m')

    def mostrar_bichinho(self):
        print(f'{self.cor}{self.bichinho}\033[m')

    def mudar_cor(self):
        self.cor = self.nova_cor()

    def sortear_bichinho(self):
        return choice(self.bichinhos_disponiveis)


bicho = Bichinho()
jogo = JogoParImpar(bichinho=bicho)
while True:
    print('''\033[1:33:40m   Menu  \033[m
    \033[1:30m[1] mudar cor do bichinho
    [2] jogar
    [3] sair\033[m''')
    opcaoo = leiaint('Sua opção: ')
    if opcaoo == 1:
        jogo.bichinhoo.mudar_cor()
        print('-' * 80)
    elif opcaoo == 2:
        jogo.iniciar_jogo()
        print('-' * 80)
    elif opcaoo == 3:
        print('-' * 80)
        break
