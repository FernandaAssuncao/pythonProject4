from time import sleep


class Calculadora:
    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0
        self.resul = 0
        self.div = []

    def soma(self):
        self.resul = self.numero1 + self.numero2
        print(f'{self.numero1} + {self.numero2} = {self.resul}')

    def subtracao(self):
        self. resul = self.numero1 - self.numero2
        print(f'{self.numero1} - {self.numero2} = {self.resul}')

    def multiplicar(self):
        self.resul = self.numero1 * self.numero2
        print(f'{self.numero1} X {self.numero2} = {self.resul}')

    def __mostrar_divisores(self, lista_num):
        for c in range(0, len(lista_num)):
            texto = f'Os divisores de {lista_num[c]} sao '
            for i in range(0, len(self.div[c])):
                texto += f'{self.div[c][i]}, '
            print(texto)
            texto = ''

    def primo_ou_nao(self):
        if len(self.div) == 0:
            self.divisores()
        for c in self.div:
            if len(c) == 2:
                print(f'O numero é primo')
            else:
                print(f'O numero não é primo')

    def divisores(self):
        lista = [self.numero1, self.numero2]
        div = []
        for item in lista:
            for c in range(1, item + 1):
                if item % c == 0:
                    div.append(c)
            self.div.append(div.copy())
            div.clear()
        self.__mostrar_divisores(lista)


def mudar_numero():
    num = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    calculadora.numero1 = num
    calculadora.numero2 = num2
    print('Calculando....')
    sleep(2)


calculadora = Calculadora()
while True:
    print(''' ===== CALCULADORA =====
    [1] adição
    [2] subtração
    [3] multiplicar
    [4] divisores
    [5] Primo ou nao?
    [6] Sair''')
    escolha = int(input('Sua opção: '))
    if escolha == 1:
        mudar_numero()
        calculadora.soma()
    elif escolha == 2:
        mudar_numero()
        calculadora.subtracao()
    elif escolha == 3:
        mudar_numero()
        calculadora.multiplicar()
    elif escolha == 4:
        mudar_numero()
        calculadora.divisores()
    elif escolha == 5:
        mudar_numero()
        calculadora.primo_ou_nao()
    elif escolha == 6:
        break
    else:
        print('ERRO, ESCOLHA UMA OPÇÃO VALIDA')
