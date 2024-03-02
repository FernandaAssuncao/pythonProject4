from valida import leiaint
from random import choice, randint
from time import sleep


class Jogo:
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
    def mensagem():
        lista = ['Errou feio em KKKKK',
                 'nossa foi longe em',
                 'que lindo,errando feio KKKKKKK',
                 'sabe qual o nome disso?burrice']
        return choice(lista)

    def __init__(self):
        self.numero = None
        self.numero_bichinho = None
        self.coracoes = 0
        self.tentativas = 10
        self.bichinho = Bichinho()

    def sortear_numero_bichinho(self):
        self.bichinho.mudar_bichinho(novo='{\_/}\n(•-•)\n > < ')
        print(f'{self.cores()}{self.bichinho.bichinho} calma aí tô pensando...', end='')
        sleep(4)
        print('já sei....\033[m')
        self.numero_bichinho = randint(1, 20)

    def numero_usuario(self):
        self.numero = leiaint('Digite um número entre 1 e 20: ')

    def mensagem_acerto(self):
        self.bichinho.mudar_bichinho(novo='{\_/}\n(•.•)\n/ ^ ^')
        print(f'\033[1:32m{self.bichinho.bichinho} Parabens você conseguiu\033[m')
        print(f'Eu escolhi o número \033[1:31m{self.numero_bichinho}\033[m')
        print(f'Você precisou de \033[1:34m{10 - self.tentativas}\033[m tentativas!!')

    def mensagem_erro(self):
        self.bichinho.mudar_bichinho(novo=self.bichinho.bichinhos_disponiveis[randint(0, 6)])
        print(f'{self.cores()}{self.bichinho.bichinho}{self.mensagem()}, ', end='')
        if self.numero > self.numero_bichinho:
            print('\033[1:40mvalor muito alto\033[m')
        else:
            print('\033[1:40mvalor muito baixo\033[m')

    def mensagem_sem_tentativas(self):
        self.bichinho.mudar_bichinho(novo='(\_/)\n(X.X)\n(") (")|')
        print(f'\033[1:31m{self.bichinho.bichinho} suas tentativas acabaram\033[m')

    def aumentar_coracoes(self):
        self.coracoes += 1

    def novas_tentativas(self):
        self.tentativas = 10

    def diminuir_tentativas(self):
        self.tentativas -= 1

    def mostrar_total_coracoes(self):
        print(f'Você fez \033[1:35m{self.coracoes}\033[m corações nessa partida!!\033[m')


class Bichinho:
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
            print('\033[1:31mBichinho não disponivel!\033[m')


jogo = Jogo()
while True:
    print('================== \033[1:32mInício\033[m \033[1:34mde\033[m \033[1:33mJogo\033[m ==================')
    jogo.sortear_numero_bichinho()
    while jogo.tentativas != 0:
        jogo.numero_usuario()
        jogo.diminuir_tentativas()
        if jogo.numero == jogo.numero_bichinho:
            jogo.mensagem_acerto()
            jogo.aumentar_coracoes()
            jogo.novas_tentativas()
            break
        else:
            jogo.mensagem_erro()
        print('-' * 55)
    if jogo.tentativas == 0:
        jogo.mensagem_sem_tentativas()
        jogo.novas_tentativas()
    print('=' * 55)
    resp = ' '
    while resp not in 'SsNn':
        try:
            resp = str(input('Quer continuar? [s/n] ')).strip()[0]
        except:
            print('\033[1:31mErro,digite o que se pede!!\033[m')
            continue
    if resp in 'Nn':
        break
print('-' * 55)
jogo.mostrar_total_coracoes()
