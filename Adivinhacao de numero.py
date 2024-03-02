from valida import leiaint
from random import randint, choice
from time import sleep


class Jogo_adivinhacao:
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
    def mensagens():
        lista_mensagens = ['Quase acertou!',
                           'Errou feio em KKKKKKKK',
                           'Muito burro(a) ',
                           'Meu Deus',
                           'Inteligência ZERO né?']
        return choice(lista_mensagens)

    def __init__(self, bichinho):
        self.usuario = None
        self.computador = None
        self.bichinhoo = bichinho
        self.vitoria = False

    def mudar_vitoria(self):
        self.vitoria = False

    def mudar_numero(self):
        self.usuario = leiaint('Digite um palpite(NÚMERO:): ')

    def computador_escolhe_numero(self):
        self.computador = randint(1, 50)

    def espera(self):
        self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}Calma aí.....tô pensando...', end='')
        sleep(4)
        print('Já sei\033[m')

    def verificar(self):
        if self.usuario == self.computador:
            self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
            print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho} \033[1:32mParabens você acertou\033[m')
            print(f'O número que escolhi foi {self.cores()}{self.computador}\033[m')
            self.vitoria = True
        else:
            self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
            print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}{self.mensagens()}\033[m')
            if self.usuario > self.computador:
                print('\033[1:31mNúmero muito alto\033[m')
            else:
                print('\033[1:34mNúmero muito abaixo\033[m')

    def iniciar_jogo(self):
        self.mudar_vitoria()
        self.espera()
        self.computador_escolhe_numero()
        while True:
            self.mudar_numero()
            self.verificar()
            print('-' * 55)
            if self.vitoria is True:
                break


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
        print('\033[1:31:40m   Menu de cores   \033[m')
        for c in range(0, len(lista_cores)):
            print(f'{lista_cores[c]}[{c}] ❀\033[m')
        verdade = False
        escolha = ''
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                escolha = lista_cores[opcao]
                verdade = True
            except:
                print('\033[1:31mErro,opção não disponivel\033[m')
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
                                      '{\_/}\n(•-•)\n > <',
                                      '{\_/}\n(•.•)\n/ ^ ^']

    def mudar_bichinho(self, novo):
        if novo in self.bichinhos_disponiveis:
            self.bichinho = novo
        else:
            print('\033[1:31mErro,bichinho não disponiveis\033[m')

    def mostrar_bichinho(self):
        print(f'{self.cor}{self.bichinho}\033[m')

    def sortear_bichinho(self):
        return self.bichinhos_disponiveis[randint(1, 6)]

    def mudar_cor(self):
        self.cor = self.nova_cor()


bicho = Bichinho()
jogo = Jogo_adivinhacao(bichinho=bicho)
while True:
    print('''\033[1:34:40m   Menu   \033[m
    \033[1:30m[1] Mudar cor do bichinho
    [2] jogar
    [3] sair\033[m''')
    opcao = leiaint('Sua opção: ')
    if opcao == 1:
        jogo.bichinhoo.mudar_cor()
        print('-' * 55)
    elif opcao == 2:
        jogo.iniciar_jogo()
        print('-' * 55)
    elif opcao == 3:
        print('-' * 55)
        break
    else:
        print('\033[1:31mErro,opção não disponivel\033[m')
