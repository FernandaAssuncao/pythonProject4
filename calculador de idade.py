from valida import leiaint
from datetime import datetime
from time import sleep
from random import choice


class CalculadoraIdade:
    @staticmethod
    def __pegar_ano_atual():
        return datetime.today().year

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
        self.ano_atual = self.__pegar_ano_atual()
        self.ano_nacimento = None
        self.idade = None
        self.bichinhoo = bichinho

    def mudar_ano_nacimento(self):
        self.ano_nacimento = leiaint('Ano de nacimento? ')

    def espera(self):
        self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}Aguarde calculando idade....\033[m')
        sleep(4)

    def calcular_idade(self):
        try:
            self.idade = self.ano_atual - self.ano_nacimento
        except:
            print('\033[1:31mErro,digite corretamente o que se pede\033[m')

    def mostrar_idade(self):
        self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}Você tem {self.idade} anos,certo?\033[m')


class Bichinho:
    @staticmethod
    def __nova_cor():
        lista = ['\033[1:30m',
                 '\033[1:31m',
                 '\033[1:32m',
                 '\033[1:33m',
                 '\033[1:34m',
                 '\033[1:35m',
                 '\033[1:36m',
                 '\033[1:37m']
        print('\033[1:34:40m  Menu de opção  \033[m')
        for c in range(0, len(lista)):
            print(f'{lista[c]}[{c}] X\033[m')
        verdade = False
        escolha = None
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                escolha = lista[opcao]
                verdade = True
            except:
                print('\033[1:31mOpção invalida\033[m')
            if verdade is True:
                print('\033[1:32mCor do bichinho alterada com sucesso\033[m')
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
calculadora = CalculadoraIdade(bichinho=bicho)
while True:
    print('''\033[1:35:40m   Menu   \033[m
    \033[1:30m[1] Mudar cor do bichinho
    [2] Mudar ano de nacimento
    [3] Calcular e mostrar idade
    [4] Sair\033[m''')
    opcaoo = leiaint('Sua opção: ')
    if opcaoo == 1:
        calculadora.bichinhoo.mudar_cor()
        print('-' * 55)
    elif opcaoo == 2:
        calculadora.mudar_ano_nacimento()
        print('-' * 55)
    elif opcaoo == 3:
        calculadora.espera()
        calculadora.calcular_idade()
        calculadora.mostrar_idade()
        print('-' * 55)
    elif opcaoo == 4:
        print('-' * 55)
        break
    else:
        print('\033[1:31mErro,opção invalida\033[m')
        print('-' * 55)
