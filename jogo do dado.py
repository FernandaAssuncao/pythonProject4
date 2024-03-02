from valida import leiaint
from random import randint, choice
from time import sleep


class Jogo_do_dado:
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
    def mensagens_vitoria():
        lista = ['ebaaaaa você acertou',
                 'VOCÊ É MUITO BOMMMM',
                 'nossa que gênio',
                 'incrivel']
        return choice(lista)

    @staticmethod
    def mensagens_derrota():
        lista = ['anão você errou',
                 'aff é muito dificil né!?',
                 'kkkkkkk karalho...',
                 'que dado chato']
        return choice(lista)

    def __init__(self, bichinho):
        self.usuario = None
        self.dado = None
        self.acertos = 0
        self.bichinhoo = bichinho

    def espera(self):
        self.bichinhoo.mudar_bichinho(self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}Agurde dado girando....\033[m')
        sleep(4)

    def escolha_usuario(self):
        verdade = False
        while True:
            numero = leiaint('Digite um número entre 1 e 6: ')
            if (numero >= 1) and (numero <= 6):
                self.usuario = numero
                break

    def girar_dado(self):
        self.dado = randint(1, 6)

    def analisar_vitoria(self):
        if self.usuario == self.dado:
            self.bichinhoo.mudar_bichinho(novo='(\_/)\n(0_0)\nC(")(")')
            print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho} \033[1:32m{self.mensagens_vitoria()}\033[m')
            print(f'o número que caiu no dado foi {self.cores()}{self.dado}\033[m')
            self.aumentar_acertos()
        else:
            self.bichinhoo.mudar_bichinho(novo='(\_/)\n(X.X)\n(") (")|')
            print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho} \033[1:31m{self.mensagens_derrota()}\033[m')
            print(f'O número que caiu no dado foi {self.cores()}{self.dado}\033[m')
        sleep(2)

    def aumentar_acertos(self):
        self.acertos += 1

    def mostrar_acertos(self):
        if self.acertos > 6:
            self.bichinhoo.mudar_bichinho(novo=' /)/)\n(^.^)\nC(")(")')
        elif self.acertos < 6:
            self.bichinhoo.mudar_bichinho(novo='(\ /)\n(* *)\nC(")(")')
        elif self.acertos > 10:
            self.bichinhoo.mudar_bichinho(novo='(\_/)\n(0_0)\nC(")(")')
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m você acertou {self.cores()}{self.acertos}\033[m vezes')

    def jogar(self):
        self.girar_dado()
        self.espera()
        self.escolha_usuario()
        self.analisar_vitoria()



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
        print('\033[1:35:40m   Menu de cores   \033[m')
        for c in range(0, len(lista_cores)):
            print(f'{lista_cores[c]}[{c}] ❤\033[m')
        verdade = False
        cor = ''
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                cor = lista_cores[opcao]
                verdade = True
            except:
                print('\033[1:31mOpção invalida\033[m')
            if verdade is True:
                print('\033[1:32mCor do bichinho alterado com sucesso!\033[m')
                return cor

    def __init__(self):
        self.bichinho = '(\_/)\n(0_0)\nC(")(")\033[m'
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
            print('\033[1:31mBichinho não disponivel\033')

    def mudar_cor(self):
        self.cor = self.nova_cor()

    def mostrar_bichinho(self):
        print(f'{self.cor}{self.bichinho}\033[m')

    def sortear_bichinho(self):
        escolha = randint(0, 6)
        return self.bichinhos_disponiveis[escolha]


bicho = Bichinho()
jogo = Jogo_do_dado(bichinho=bicho)
while True:
    print('''\033[1:34:40m   Menu de opções   \033[m
    \033[1:30m[1] jogar
    [2] mudar cor do bichinho
    [3] ver bichinho
    [4] mostrar quantidade de acertos
    [5] sair\033[m''')
    opcao = leiaint('Sua opção: ')
    if opcao == 1:
        jogo.jogar()
        print('-' * 60)
    elif opcao == 2:
        jogo.bichinhoo.mudar_cor()
        print('-' * 60)
    elif opcao == 3:
        jogo.bichinhoo.mostrar_bichinho()
        print('-' * 60)
    elif opcao == 4:
        jogo.mostrar_acertos()
        print('-' * 60)
    elif opcao == 5:
        break
