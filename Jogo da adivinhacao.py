from valida import leiaint
from random import randint, choice
from datetime import datetime
from pytz import timezone


class Jogo_adivinhacao:
    @staticmethod
    def data_e_hora():
        fuso_br = timezone('brazil/East')
        horario = datetime.now(fuso_br)
        return horario.strftime('%d/%m/%Y %H:%M:%S')

    @staticmethod
    def mensagens_de_erro():
        lista = ['aff',
                 'anda não tá dificil',
                 'vai você comsegue',
                 'larga de ser burro(a)',
                 'anão']
        return choice(lista)

    @staticmethod
    def cores():
        lista_cores = ['\033[1:31m',
                       '\033[1:33m',
                       '\033[1:35m',
                       '\033[1:36m']
        return choice(lista_cores)

    @staticmethod
    def bichinho_mensagem_erro():
        return randint(0, 4)

    def __init__(self, bichinho):
        self.usuario = None
        self.computador = None
        self.nivel_de_dificuldade = False
        self.tentativas = 0
        self.bichinhoo = bichinho
        self.historico = []

    def mudar_numero(self):
        self.usuario = leiaint('Seu palpite entre 1 e 40: ')
        self.aumentar_tentativas()

    def sortear_numero_computador(self):
        self.computador = randint(1, 40)

    def aumentar_tentativas(self):
        self.tentativas += 1

    def adicionar_ao_historico(self):
        self.historico.append((self.data_e_hora(),
                               self.computador,
                               self.tentativas))

    def deletar_tentativas(self):
        self.tentativas = 0

    def mensagens(self):
        self.bichinhoo.mudar_bichinho(novo='{\_/}\n(•.•)\n/ > ❤')
        if self.usuario == self.computador:
            self.adicionar_ao_historico()
            print(F'\033[1:32m{self.bichinhoo.bichinho} Parabens você acertou!!\033[m')
            print(f'Eu escolhi o número \033[1:35m{self.computador}\033[m!')
            print(f'Você conseguiu com {self.cores()}{self.tentativas}\033[m tentativas!!')
            self.deletar_tentativas()
        else:
            c = Jogo_adivinhacao.bichinho_mensagem_erro()
            self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.bichinhos_disponiveis[c])
            print(f'{self.cores()}{self.bichinhoo.bichinho} {Jogo_adivinhacao.mensagens_de_erro()}\033[m')
            if self.usuario > self.computador:
                print('\033[1:31mvalor muito alto!!\033[m')
            else:
                print('\033[1:34mvalor muito baixo!!\033[m')


class Bichinhos:
    def __init__(self):
        self.bichinho = '(\_/)\n(0_0)\nC(")(")'
        self.bichinhos_disponiveis = ['(\_/)\n(0_0)\nC(")(")',
                                      ' /)/)\n(^.^)\nC(")(")',
                                      '(\_/)\n(X.X)\n(") (")|',
                                      '(\ /)\n(. .)\nC(")(")',
                                      '( Y )\n( 0 0)\no(")(")',
                                      '{\_/}\n(•-•)\n❤ <',
                                      '{\_/}\n(•.•)\n/ > ❤']

    def mudar_bichinho(self, novo):
        if novo in self.bichinhos_disponiveis:
            self.bichinho = novo
        else:
            print('\033[1:31mErro,bichinho não disponivel!\033[m')


bicho = Bichinhos()
jogo = Jogo_adivinhacao(bichinho=bicho)
while True:
    print('----------------- \033[1:34:40m  Início \033[1:31mde\033[1:35m jogo  \033[m ------------------')
    jogo.sortear_numero_computador()
    while jogo.usuario != jogo.computador:
        jogo.mudar_numero()
        jogo.mensagens()
        print('-' * 45)
    resp = ' '
    while resp not in 'SsNn':
        try:
            resp = str(input('Quer continuar? [s/n] ')).strip()[0]
        except:
            print('\033[1:31mErro,por favor digite o que se pede!!\033[m')
            continue
    print('-' * 65)
    if resp in 'Nn':
        break
