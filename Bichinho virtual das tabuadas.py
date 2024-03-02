from valida import leiaint
from time import sleep
from random import choice


class Tabuada:
    @staticmethod
    def cores():
        lista_cores = ['\033[1:33m',
                       '\033[1:34m',
                       '\033[1:35m',
                       '\033[1:36m']
        return choice(lista_cores)

    def __init__(self, bichinho):
        self.numero = None
        self.tabuada = []
        self.bichinhoo = bichinho

    def mensagem_de_fim(self):
        self.bichinhoo.mudar_bichinho(novo_bichinho='(\_/)\n(0_0)\nC(")(")')
        print(f'{Tabuada.cores()}{self.bichinhoo.bichinho} até que fim terminou!\033[m')

    def espera(self):
        self.bichinhoo.mudar_bichinho(novo_bichinho='(\_/)\n(X.X)\n(") (")|')
        print(f'{Tabuada.cores()}{self.bichinhoo.bichinho} aff vou ter que pensar!!\033[m')
        sleep(5)

    def mudar_numero(self):
        self.numero = leiaint('Digite um número INTEIRO: ')
        print('\033[1:32mNúmero alterado com sucesso!\033[m')
        self.tabuada.clear()

    def __tabuada_do_numero(self):
        for c in range(1, 11):
            self.tabuada.append(self.numero * c)

    def mostrar_tabuada(self):
        if self.numero is not None:
            self.__tabuada_do_numero()
            i = 1
            for c in self.tabuada:
                print(f'{self.cores()}{self.numero}\033[m x {self.cores()}{i}\033[m = \033[1:31m{c}\033[m')
                i += 1
                sleep(1)
        else:
            print('\033[1:31mErro,mude o número para um valor inteiro!!\033[m')



class Bichinho:
    def __init__(self):
        self.bichinho = '(\_/)\n(0_0)\nC(")(")'
        self.bichinhos_disponiveis = ['(\_/)\n(0_0)\nC(")(")',
                                      ' /)/)\n(^.^)\nC(")(")',
                                      '(\_/)\n(X.X)\n(") (")|',
                                      '(\ /)\n(. .)\nC(")(")',
                                      '( Y )\n( 0 0)\no(")(")']

    def mudar_bichinho(self, novo_bichinho):
        if novo_bichinho in self.bichinhos_disponiveis:
            self.bichinho = novo_bichinho
        else:
            print('\033[1:31mErro,bichinho não disponivel\033[m')


bicho = Bichinho()
tabuada = Tabuada(bichinho=bicho)
while True:
    print('''\033[1:31:40m  Menu \033[m
    \033[1:30m[1] mudar número
    [2] mostrar tabuada
    [3] sair\033[m''')
    opcao = leiaint('Sua opção: ')
    if opcao == 1:
        tabuada.mudar_numero()
        print('-' * 45)
    elif opcao == 2:
        tabuada.espera()
        tabuada.mostrar_tabuada()
        tabuada.mensagem_de_fim()
        print('-' * 45)
    elif opcao == 3:
       break
    else:
        print('\033[1:31mOpção não disponivel\033[m')
