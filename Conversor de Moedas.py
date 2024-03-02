from valida import leiafloat, leiaint
from time import sleep
from random import choice
import requests


link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'


class ConversorMoedas:
    @staticmethod
    def cores():
        lista_cores = ['\033[1:30m',
                       '\033[1:31m',
                       '\033[1:32m',
                       '\033[1:33m',
                       '\033[1:34m',
                       '\033[1:35m',
                       '\033[1:36m',
                       '\033[1:37m']
        return choice(lista_cores)

    def __init__(self, bichinho):
        self.moeda_escolhida = None
        self.valor_moeda = None
        self.moedas_disponiveis = []
        self.moedas = []
        self.bichinhoo = bichinho

    def alterar_lista(self):
        requisicao = requests.get(f'{link}')
        dic = requisicao.json()
        for item in dic:
            self.moedas_disponiveis.append(item)
            self.moedas.append((item, dic[item]['bid']))

    def escolher_moeda(self):
        for c in range(0, len(self.moedas_disponiveis)):
            print(f'{self.cores()}[{c}] {self.moedas_disponiveis[c]}\033[m')
        verdade = False
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                escolha = self.moedas_disponiveis[opcao]
                self.moeda_escolhida = escolha
                self.__mudar_valor_moeda()
                verdade = True
            except:
                print('\033[1:31mErro,Opção Invalida\033[m')
            if verdade is True:
                self.bichinhoo.mudar_bichinho(novo='(\_/)\n(0_0)\nC(")(")')
                print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m {self.cores()}Aguarde procurando cotações....\033[m')
                sleep(4)
                print('\033[1:32mMoeda alterada com sucesso!\033[m')
                break

    def __mudar_valor_moeda(self):
        try:
            for moeda, valor in self.moedas:
                if moeda == self.moeda_escolhida:
                    self.valor_moeda = float(valor)
        except:
            print('\033[1:31mAlgo deu errado :(\033[m')

    def __converter_moeda_para_real(self, valor_moeda):
        return self.valor_moeda * valor_moeda

    def mostrar_valor(self):
        moeda = leiafloat('Qual valor? ')
        result = self.__converter_moeda_para_real(valor_moeda=moeda)
        self.bichinhoo.mudar_bichinho(novo=self.bichinhoo.sortear_bichinho())
        print(f'{self.bichinhoo.cor}{self.bichinhoo.bichinho}\033[m{self.cores()}{self.moeda_escolhida} {moeda}\033[m = R${self.cores()}{result:.2f}\033[m')


class Bichinho:
    @staticmethod
    def nova():
        lista_cores = ['\033[1:30m',
                       '\033[1:31m',
                       '\033[1:32m',
                       '\033[1:33m',
                       '\033[1:34m',
                       '\033[1:35m',
                       '\033[1:36m',
                       '\033[1:37m']
        for c in range(0, len(lista_cores)):
            print(f'{lista_cores[c]}[{c}] &\033[m')
        verdade = False
        escolha = None
        while True:
            try:
                opcao = leiaint('Sua opção: ')
                escolha = lista_cores[opcao]
                verdade = True
            except:
                print('\033[1:31mOpção invalida\033[m')
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

    def sortear_bichinho(self):
        return choice(self.bichinhos_disponiveis)

    def mostrar_bichinho(self):
        print(f'{self.cor}{self.bichinho}\033[m')

    def mudar_cor(self):
        self.cor = self.nova()


bicho = Bichinho()
conversor = ConversorMoedas(bichinho=bicho)
conversor.alterar_lista()
while True:
    print('''\033[1:35:40m   Menu de opções  \033[m
    \033[1:30m[1] Mudar cor do bichinho
    [2] Alterar Moeda
    [3] Converter moeda para real
    [4] Sair\033[m''')
    opcaoo = leiaint('Sua opção: ')
    if opcaoo == 1:
        conversor.bichinhoo.mudar_cor()
        print('-' * 55)
    elif opcaoo == 2:
        conversor.escolher_moeda()
        print('-' * 55)
    elif opcaoo == 3:
        conversor.mostrar_valor()
        print('-' * 55)
    elif opcaoo == 4:
        print('-' * 55)
        break
    else:
        print('\033[1:31mErro,opção Invalida !\033[m')
        print('-' * 55)
