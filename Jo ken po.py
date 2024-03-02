from valida import leiaint
from random import randint, choice
from time import sleep


class Jokenpo:
    @staticmethod
    def __validacao():
        lista = ['pedra',
                 'papel',
                 'tesoura']
        print('\033[1:30m-\033[m' * 13)
        print('\033[1:34:40m  Menu  \033[m')
        for c in range(0, len(lista)):
            print(f'\033[1:30m[{c}] {lista[c]}\033[m')
        print('\033[1:30m-\033[m' * 13)
        verdade = False
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                escolha = lista[opcao]
                verdade = True
            except:
                print('\033[1:31mOpção invalida\033[m')
                continue
            if verdade is True:
                return escolha

    @staticmethod
    def __validacao2():
        lista = ['pedra',
                 'papel',
                 'tesoura']
        return lista[randint(0, 2)]

    @staticmethod
    def cores():
        lista = ['\033[1:31m',
                 '\033[1:32m',
                 '\033[1:33m',
                 '\033[1:34m',
                 '\033[1:35m',
                 '\033[1:36m']
        return choice(lista)

    def __init__(self, bichinho):
        self.computador = None
        self.usuario = None
        self.bichinhoo = bichinho
        self.vencedor = None

    def escolha_usuario(self):
       self.usuario = self.__validacao()

    def escolha_computador(self):
        self.computador = self.__validacao2()

    def mensagem_jo_ken_po(self):
       self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.bichinhos_disponiveis[randint(0, 6)])
       print(f'\033[1:35m{self.bichinhoo.bichinho}\033[m')
       sleep(1)
       print(f'{self.cores()}JÓ\033[m')
       sleep(1)
       print(f'{self.cores()}KEN\033[m ')
       sleep(1)
       print(f'{self.cores()}PÔ\033[m')
       sleep(0.5)

    def mostrar_escolhas(self):
        print(f'O computador escolheu {self.cores()}{self.computador}!!\033[m')
        print(f'Você escolheu {self.cores()}{self.usuario}!!\033[m')

    def verificar_quem_sera_o_vencedor(self):
        if (self.usuario == 'pedra') and (self.computador == 'pedra'):
            self.vencedor = 'empate'
        elif (self.usuario == 'pedra') and (self.computador == 'papel'):
            self.vencedor = 'computador'
        elif (self.usuario == 'pedra') and (self.computador == 'tesoura'):
            self.vencedor = 'usuario'
        elif (self.usuario == 'papel') and (self.computador == 'pedra'):
            self.vencedor = 'usuario'
        elif (self.usuario == 'papel') and (self.computador == 'papel'):
            self.vencedor = 'empate'
        elif (self.usuario == 'papel') and (self.computador == 'tesoura'):
            self.vencedor = 'computador'
        elif (self.usuario == 'tesoura') and (self.computador == 'pedra'):
            self.vencedor = 'computador'
        elif (self.usuario == 'tesoura') and (self.computador == 'papel'):
            self.vencedor = 'usuario'
        elif (self.usuario == 'tesoura') and (self.computador == 'tesoura'):
            self.vencedor = 'empate'

    def mostrar_resultados(self):
        if self.vencedor == 'usuario':
            self.bichinhoo.mudar_bichinho(novo='(\_/)\n(0_0)\nC(")(")')
            print(f'\033[1:32m{self.bichinhoo.bichinho}\033[1:32:40m  Vencedor: {self.vencedor}  \033[m')
        elif self.vencedor == 'computador':
            self.bichinhoo.mudar_bichinho(novo='(\_/)\n(X.X)\n(") (")|')
            print(f'\033[1:31m{self.bichinhoo.bichinho}\033[1:31:40m  Vencedor: {self.vencedor}  \033[m')
        else:
            self.bichinhoo.mudar_bichinho(novo='{\_/}\n(•-•)\n > < ')
            print(f'\033[1:33m{self.bichinhoo.bichinho}\033[1:33:40m  Vencedor: {self.vencedor}  \033[m')


class Bichinho:
    def __init__(self):
        self.bichinho = '(\_/)\n(0_0)\nC(")(")'
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


bicho = Bichinho()
jogo = Jokenpo(bichinho=bicho)
while True:
    jogo.bichinhoo.mudar_bichinho(novo=' /)/)\n(^.^)\nC(")(")')
    print(f'\033[1:35m{jogo.bichinhoo.bichinho} \033[1:34mInício \033[1:30mde \033[1:37mJogo\033[m ---------')
    jogo.escolha_usuario()
    jogo.escolha_computador()
    jogo.mensagem_jo_ken_po()
    jogo.mostrar_escolhas()
    jogo.verificar_quem_sera_o_vencedor()
    jogo.mostrar_resultados()
    sleep(1)
    print('=' * 55)
    resp = ' '
    while resp not in 'SsNn':
        try:
            resp = str(input('Quer continuar jogando? [s/n] ')).strip()[0]
        except:
            print('\033[1:31mErro,por favor digite o que se pede\033[m')
            continue
    print('=' * 55)
    if resp in 'Nn':
        break
