from random import randint, choice
from valida import leiaint
from time import sleep
from datetime import datetime
from pytz import timezone


class Simulador_dado:
    @staticmethod
    def cores():
        lista_cores = ['\033[1:31m',
                       '\033[1:32m',
                       '\033[1:33m',
                       '\033[1:34m',
                       '\033[1:35m',
                       '\033[1:36m']
        return choice(lista_cores)

    @staticmethod
    def dh():
        fuso_br = timezone('brazil/East')
        horario = datetime.now(fuso_br)
        return horario.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, bichinhoo):
        self.dado = None
        self.bichinhoo = bichinhoo
        self.historico = []

    def niveis(self):
        if self.dado is not None:
            if self.dado == 6:
                self.bichinhoo.mudar_bichinho(novo='(\_/)\n(0_0)\nC(")(")')
            elif (self.dado >= 4) and (self.dado <= 5):
                self.bichinhoo.mudar_bichinho(novo='{\_/}\n(•-•)\n > < ')
            else:
                self.bichinhoo.mudar_bichinho(novo='(\ /)\n(* *)\nC(")(")')

    def dado_girando(self):
        self.dado = randint(1, 6)

    def espera_dado_girando(self):
        self.bichinhoo.mudar_bichinho(novo='(\_/)\n(X.X)\n(") (")|')
        print(f'{self.cores()}{self.bichinhoo.bichinho} aguarde dado girando....\033[m')
        sleep(2)

    def mostrar_numero_que_caiu_no_dado(self):
        self.niveis()
        print(f'{self.cores()}{self.bichinhoo.bichinho}\033[m O número que caiu no dado foi {self.cores()}{self.dado}\033[m')

    def adicionar_ao_historico(self):
        self.historico.append((self.dado,
                               self.dh()))

    def mostrar_historico(self):
        '''

        Função que mostra o historico onde está amazernado
         data e hora em que o dado foi girado
        :return: não retorna nenhum valor

        '''
        print('=================== \033[1:36mHistorico\033[m ==================')
        self.bichinhoo.mudar_bichinho(novo='{\_/}\n(•.•)\n/ ^ ^')
        print(f'\033[1:35m{self.bichinhoo.bichinho} número que caiu no dado mais data e hora\033[m')
        for n, d in self.historico:
            print(f'\033[1:34m{n:<15}\033[m {d}')



class Bichinho:
    def __init__(self):
        self.bichinho = '(\_/)\n(0_0)\nC(")(")'
        self.bichinhos_disponivel = ['(\_/)\n(0_0)\nC(")(")',
                                      ' /)/)\n(^.^)\nC(")(")',
                                      '(\_/)\n(X.X)\n(") (")|',
                                      '(\ /)\n(* *)\nC(")(")',
                                      '( Y )\n( 0 0)\no(")(")',
                                      '{\_/}\n(•-•)\n > < ',
                                      '{\_/}\n(•.•)\n/ ^ ^']

    def mudar_bichinho(self, novo):
        if novo in self.bichinhos_disponivel:
            self.bichinho = novo
        else:
            print('\033[1:31mBichinho não disponivel\033[m')


bicho = Bichinho()
simulador = Simulador_dado(bichinhoo=bicho)
while True:
    print(''' \033[1:31:40m   Menu  \033[m
    \033[1:30m[1] girar dado
    [2] historico
    [3] sair\033[m''')
    opcao = leiaint('Sua opção: ')
    if opcao == 1:
        simulador.dado_girando()
        simulador.espera_dado_girando()
        simulador.mostrar_numero_que_caiu_no_dado()
        simulador.adicionar_ao_historico()
        print('-' * 45)
    elif opcao == 2:
        simulador.mostrar_historico()
        print('-' * 45)
    elif opcao == 3:
        print('-' * 45)
        break
