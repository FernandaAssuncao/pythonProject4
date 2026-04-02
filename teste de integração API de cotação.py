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
        print(self.moedas)
        print(self.moedas_disponiveis)


cotacao = SistemaDeCotacao()
