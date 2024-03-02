from valida import leiaint
from time import sleep
from datetime import datetime
from random import choice, randint
from pytz import timezone


class Contador_de_segundos:
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
    def mensagem_fim():
        lista = ['teminei a contagem mamãe/papai',
                 'TERMINEI ESSA MERDA!!',
                 'ACABEI AQUI',
                 'FIM....']
        return choice(lista)

    @staticmethod
    def data_hora():
        fuso_br = timezone('brazil/East')
        horario = datetime.now(fuso_br)
        return horario.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, bichinho):
        self.segundos = None
        self._inicio_contagem = None
        self._tipo_de_contagem = False
        self._fim_contagem = None
        self._bichinhoo = bichinho

    def inicio_contagemm(self):
        self._inicio_contagem = self.data_hora()

    def fim_contagemm(self):
        self._fim_contagem = self.data_hora()

    def mensagem_engracada(self):
        if self.segundos <= 120:
            self._bichinhoo.mudar_bichinho(novo='{\_/}\n(•-•)\n > < ')
            print(f'{self.cores()}{self._bichinhoo.bichinho} 1 minuto, 2 não é muito não?\033[m ')
        elif (self.segundos > 120) and (self.segundos <= 900):
            self._bichinhoo.mudar_bichinho(novo='(\_/)\n(0_0)\nC(")(")')
            print(f'{self.cores()}{self._bichinhoo.bichinho} muito tempo da minha vida contando pra você, não acha não?\033[m')
        else:
            self._bichinhoo.mudar_bichinho(novo='(\_/)\n(X.X)\n(") (")|')
            print(f'{self.cores()}{self._bichinhoo.bichinho} vou te denunciar pro conselho tutelar,por abuso de filho\033[m')

    def mudar_numero(self, novo_numero):
        self.segundos = novo_numero
        print(f'\033[1:32mSegundos alterados para {self.segundos} com sucesso!!\033[m')

    def inicar_contagem(self):
        self.mensagem_engracada()
        self.inicio_contagemm()
        if self._tipo_de_contagem is False:
            for c in range(1, self.segundos + 1):
                print(f'{self.cores()}{c}\033[m, ', end='')
                sleep(1)
        else:
            for c in range(self.segundos, 0, -1):
                print(f'{self.cores()}{c}\033[m, ', end='')
                sleep(1)
        self.fim_contagemm()
        print()
        self._bichinhoo.mudar_bichinho(novo=self._bichinhoo.bichinhos_disponiveis[randint(1, 6)])
        print(f'{self.cores()}{self._bichinhoo.bichinho} {self.mensagem_fim()}\033[m')

    def normal(self):
        self._tipo_de_contagem = False
        print('\033[1:32mTipo de contagem alterado com sucesso!\033[m')

    def regressiva(self):
        self._tipo_de_contagem = True
        print('\033[1:32mTipo de contagem alterado com sucesso!\033[m')

    def mostrar_detalhes(self):
        print('--- \033[1:35:40m  Detalhes  \033[m ---')
        self._bichinhoo.mudar_bichinho(novo=' /)/)\n(^.^)\nC(")(")')
        print(f'{self.cores()}{self._bichinhoo.bichinho}\033[m')
        print(f'\033[1:30mSegundos: {self.segundos}')
        print(f'Início Contagem: {self._inicio_contagem}')
        print(f'Fim contagem: {self._fim_contagem}')
        print(f'Contagem regressiva: {self._tipo_de_contagem}\033[m')
        print('-' * 45)


class Bichinhos:
    def __init__(self):
        self.bichinho = '(\_/)\n(0_0)\nC(")(")'
        self.bichinhos_disponiveis = ['(\_/)\n(0_0)\nC(")(")',
                                      ' /)/)\n(^.^)\nC(")(")',
                                      '(\_/)\n(X.X)\n(") (")|',
                                      '(\ /)\n(. .)\nC(")(")',
                                      '( Y )\n( 0 0)\no(")(")',
                                      '{\_/}\n(•-•)\n > < ',
                                      '{\_/}\n(•.•)\n/ ^ ^']

    def mudar_bichinho(self, novo):
        if novo in self.bichinhos_disponiveis:
            self.bichinho = novo
        else:
            print('\033[1:31mErro,bichinho não disponivel\033[m')


bicho = Bichinhos()
contador = Contador_de_segundos(bichinho=bicho)
while True:
    print('''\033[1:31:40m  Menu \033[m
    \033[1:30m[1] mudar segundos
    [2] contagem normal
    [3] contagem regressiva
    [4] iniciar contagem
    [5] ver detalhes
    [6] sair\033[m''')
    opcao = leiaint('Sua opção: ')
    if opcao == 1:
        contador.mudar_numero(novo_numero=leiaint('Segundos....'))
        print('-' * 60)
    elif opcao == 2:
        contador.normal()
        print('-' * 60)
    elif opcao == 3:
        contador.regressiva()
        print('-' * 60)
    elif opcao == 4:
        contador.inicar_contagem()
        print('-' * 60)
    elif opcao == 5:
        contador.mostrar_detalhes()
        print('-' * 60)
    elif opcao == 6:
        print('-' * 60)
        break
    else:
        print('\033[1:31mErro,opção invalida\033[m')
        print('-' * 60)
