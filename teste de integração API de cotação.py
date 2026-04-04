import requests
import copy


class SistemaDeCotacao:
    def __init__(self):
        self.moedas_disponiveis = []
        self.moeda = None
        self.moedas = []
        self.__link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
        self.__pegar_moeda()

    def __pegar_moeda(self):
        requisicao = requests.get(self.__link)
        dic = requisicao.json()
        for item in dic.keys():
            lista = [item, float(dic[item]['bid'])]
            self.moedas_disponiveis.append(item)
            self.moedas.append(copy.deepcopy(lista))

    def ver_moedas(self):
        texto = 'As moedas disponiveis são: '
        for moedas in self.moedas_disponiveis:
            texto += f'\033[1:35m{moedas}, '
        print(f'{texto}\033[m')
        print('=' * 30)

    def escolher_moeda(self):
        try:
            escolha = str(input('Digite sua escolha: ')).strip().upper()
            if escolha in self.moedas_disponiveis:
                self.moeda = escolha
                print(f'\033[1:32mMoeda escolhida com sucesso!!{self.moeda}\033[m')
            else:
                raise
        except:
            print('\033[1:31mEscolha invalida!\033[m')
        print('=' * 30)

    def ver_cotacao(self):
        try:
            if self.moeda is None:
                raise
            else:
                for moeda in self.moedas:
                    if moeda[0] == self.moeda:
                        print(f'\033[1:36mA cotação da {moeda[0]} é {moeda[1]:.2f}\033[m')
        except:
            print('\033[1:31mERRO, escolha uma moeda primeiro!!\033[m')
        print('=' * 30)


cotacao = SistemaDeCotacao()
while True:
    print('''\033[1:34mSISTEMA DE COTAÇÃO
    [1] Ver moedas disponiveis
    [2] Escolher moeda
    [3] Ver cotação
    [4] Sair\033[m''')
    opcao = int(input('Digite sua opção: '))
    print('=' * 30)
    if opcao == 1:
        cotacao.ver_moedas()
    elif opcao == 2:
        cotacao.escolher_moeda()
    elif opcao == 3:
        cotacao.ver_cotacao()
    elif opcao == 4:
        break

