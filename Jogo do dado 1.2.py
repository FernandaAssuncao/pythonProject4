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

    def __init__(self, bichinho):
        self.bichinhoo = bichinho
        self.dado = None
        self.usuario = None
        self.computador = None
        self.vencedor = None

    def espera(self):
        self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}Aguarde dado girando....', end='')
        sleep(4)
        print('CAIU\033[m')

    def girar_dado(self):
        self.dado = randint(1, 6)

    def escolha_usuario(self):
        self.usuario = leiaint('Chute um número entre  1 e 6: ')

    def escolha_computador(self):
        self.computador = randint(1, 6)

    def mostrar_escolhas(self):
        self.bichinhoo.mudar_bichinho(novo='{\_/}\n(•-•)\n > < ')
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m você chutou {self.cores()}{self.usuario}\033[m')
        print(f'E o computador chutou {self.cores()}{self.computador}\033[m')

    def mostrar_numero_do_dado(self):
        print(f'O número que caiu no dado foi {self.cores()}{self.dado}\033[m')

    def quem_acertou(self):
        if self.usuario == self.dado:
            self.vencedor = 'você'
        elif self.computador == self.dado:
            self.vencedor = 'computador'
        else:
            self.vencedor = 'nenhum'

    def mostrar_quem_acertou(self):
        self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}quem chutou certo foi....', end='')
        sleep(6)
        print(f'{self.vencedor}\033[m')

    def jogar(self):
        self.escolha_usuario()
        self.escolha_computador()
        self.mostrar_escolhas()
        self.girar_dado()
        self.espera()
        self.mostrar_numero_do_dado()
        self.quem_acertou()
        self.mostrar_quem_acertou()


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
        print('\033[1:33:40m   Menu de escolhas  \033[m')
        for cores in range(0, len(lista_cores)):
            print(f'{lista_cores[cores]}[{cores}] ★\033[m')
        verdade = False
        cor_escolhida = ''
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                cor_escolhida = lista_cores[opcao]
                verdade = True
            except:
                print('\033[1:31mErro,cor não disponivel\033[m')
            if verdade:
                print('\033[1:32mCor alterado com sucesso!\033[m')
                return cor_escolhida

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
            print('\033[1:31mBichinho não disponivel\033[m')

    def mudar_cor(self):
       self.cor = self.nova_cor()

    def mostrar_bichinho(self):
        print(f'{self.cor}{self.bichinho}\033[m')

    def sortear_bichinho(self):
        return self.bichinhos_disponiveis[randint(0, 6)]


bicho = Bichinho()
jogo = Jogo_do_dado(bichinho=bicho)
while True:
    print('''\033[1:35:40m   Menu   \033[m
    \033[1:30m[1] mudar cor do bichinho
    [2] jogar
    [3] sair\033[m''')
    opcao = leiaint('Sua opção: ')
    if opcao == 1:
        jogo.bichinhoo.mudar_cor()
        print('-' * 55)
    elif opcao == 2:
        jogo.jogar()
        print('-' * 55)
    elif opcao == 3:
        print('-' * 55)
        break
    else:
        print('\033[1:31mErro,opção invalida\033[m')
        print('-' * 55)
