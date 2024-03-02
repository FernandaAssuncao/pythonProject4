from random import randint, choice
from valida import leiaint
from datetime import datetime
from pytz import timezone
from time import sleep


class Contador:
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
        return horario.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, bichinho):
        self.segundos = None
        self.inicio = None
        self.fim = None
        self.historico = []
        self.bichinhoo = bichinho

    def mudar_segundos(self):
        self.segundos = leiaint('Segundos....')
        print('\033[1:32mSegundos alterados com sucesso!\033[m')

    def espera(self):
        self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}Que preguiça de contar....\033[m')
        sleep(4)

    def contagem(self):
        self.__inicio_contagem()
        for c in range(1, self.segundos + 1):
            print(f'{self.cores()}{c}\033[m')
            sleep(1)
        self.__fim_contagem()
        self.__adicionar_ao_historico()

    def __inicio_contagem(self):
        self.inicio = self.data_e_hora()

    def __fim_contagem(self):
        self.fim = self.data_e_hora()

    def mostrar_informacoes(self):
        print('-' * 45)
        print(f'''\033[1:34:40m   Imformações da contagem   \033[m
        Segundos: \033[1:33m{self.segundos}\033[m
        Inicio da Contagem: \033[1:32m{self.inicio}\033[m
        Fim da Contagem: \033[1:34m{self.fim}\033[m''')
        print('-' * 45)

    def __adicionar_ao_historico(self):
        dic = {'Segundos': self.segundos,
               'Inicio Contagem': self.inicio,
               'Fim Contagem': self.fim}
        self.historico.append(dic)

    def mostrar_historico(self):
        print('=================== \033[1:35:40mMostrar Historico\033[m =================')
        for i in self.historico:
            print(f'Segundos: \033[1:35m{i["Segundos"]}\033[m')
            print(f'Inicio da Contagem: \033[1:37m{i["Inicio Contagem"]}\033[m')
            print(f'Fim da Contagem: \033[1:34m{i["Fim Contagem"]}\033[m')
            print('-' * 45)


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
            print(f'{lista_cores[c]}[{c}] ❤\033[m')
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

    def mostrar_bichinho(self):
        print(f'{self.cor}{self.bichinho}\033[m')

    def sortear_bichinho(self):
        return self.bichinhos_disponiveis[randint(0, 6)]

    def mudar_cor(self):
        self.cor = self.nova_cor()


bicho = Bichinho()
cont = Contador(bichinho=bicho)
while True:
    print('''\033[1:31:40m  Menu  \033[m
    \033[1:30m[1] Mudar Cor
    [2] Mudar Segundos
    [3] Iniciar Contagem
    [4] Mostrar Informações
    [5] Mostrar Historico
    [6] Sair\033[m''')
    opcaoo = leiaint('Sua opção: ')
    if opcaoo == 1:
        cont.bichinhoo.mudar_cor()
        print('-' * 55)
    elif opcaoo == 2:
        cont.mudar_segundos()
        print('-' * 55)
    elif opcaoo == 3:
        cont.espera()
        cont.contagem()
        print('-' * 55)
    elif opcaoo == 4:
        cont.mostrar_informacoes()
    elif opcaoo == 5:
        cont.mostrar_historico()
        print('-' * 55)
    elif opcaoo == 6:
        print('-' * 55)
        break
    else:
        print('\033[1:31mOpção invalida\033[m')
