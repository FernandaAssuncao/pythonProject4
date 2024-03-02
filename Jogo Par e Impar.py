from valida import leiaint
from random import randint, choice
from time import sleep


class ParImpar:
    @staticmethod
    def cores():
        lista_cores = ['\033[1:31m',
                       '\033[1:32m',
                       '\033[1:33m',
                       '\033[1:34m',
                       '\033[1:36m']
        return choice(lista_cores)

    def __init__(self, bichinho):
        self.usuario = None
        self.computador = None
        self.computador_numero = None
        self.usuario_numero = None
        self.vencedor = None
        self.soma = None
        self.bichinhoo = bichinho

    def mudar_usuario(self):
        lista = ['par',
                 'impar']
        print('\033[1:34:40m   Escolha das opções abaixo   \033[m')
        for c in range(0, len(lista)):
            print(f'\033[1:30m[{c}] {lista[c]}\033[m')
        verdade = False
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                item = lista[opcao]
                verdade = True
            except:
                print('\033[1:31mErro,opção invalida\033[m')
                continue
            if verdade is True:
                self.usuario = item
                break

    def computador_escolha(self):
        if self.usuario is not None:
            if self.usuario == 'par':
                self.computador = 'impar'
            else:
                self.computador = 'par'

    def mostrar_escolhas(self):
        print(f'Você escolheu {self.cores()}{self.usuario}\033[m')
        print(f'E o computador ficou com {self.cores()}{self.computador}\033[m')

    def espera(self):
        self.bichinhoo.mudar_bichinho(novo=' /)/)\n(^.^)\nC(")(")')
        print(f'{self.cores()}{self.bichinhoo.bichinho} Segunda parte....\033[m')
        sleep(2)

    def numero_usuario(self):
        self.usuario_numero = leiaint('Digite um número entre 1 e 10: ')

    def numero_computador(self):
        self.computador_numero = randint(1, 10)

    def mostrar_numeros_escolhidos(self):
        print(f'Você escolheu o número {self.cores()}{self.usuario_numero}\033[m')
        print(f'E o computador escolheu {self.cores()}{self.computador_numero}\033[m')

    def somar(self):
        self.soma = self.usuario_numero + self.computador_numero

    def mostrar_soma(self):
        self.bichinhoo.mudar_bichinho(novo='{\_/}\n(•-•)\n > < ')
        print(f'\033[1:35m{self.bichinhoo.bichinho} \033[mA soma entre os dois valores foi: {self.cores()}{self.soma}\033[m')

    def quem_sera_o_vencedor(self):
        if self.usuario == 'par':
            if self.soma % 2 == 0:
                self.vencedor = 'usuario'
            else:
                self.vencedor = 'computador'
        elif self.usuario == 'impar':
            if self.soma % 2 == 0:
                self.vencedor = 'computador'
            else:
                self.vencedor = 'usuario'

    def mostrar_vencedor(self):
        if self.vencedor == 'usuario':
            print(f'\033[1:32:40m   Vencedor: {self.vencedor}   \033[m')
        else:
            print(f'\033[1:33:40m   Vencedor: {self.vencedor}   \033[m')

    def iniciar_jogo(self):
        jogo.mudar_usuario()
        jogo.computador_escolha()
        print('-' * 55)
        jogo.mostrar_escolhas()
        print('-' * 55)
        jogo.espera()
        jogo.numero_usuario()
        jogo.numero_computador()
        print('-' * 55)
        jogo.mostrar_numeros_escolhidos()
        jogo.somar()
        jogo.mostrar_soma()
        jogo.quem_sera_o_vencedor()
        jogo.mostrar_vencedor()


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
jogo = ParImpar(bichinho=bicho)
jogo.iniciar_jogo()
