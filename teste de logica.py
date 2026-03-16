from time import sleep


class Calculadora:
    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0
        self.resul = 0

    def soma(self):
        self.resul = self.numero1 + self.numero2
        print(f'{self.numero1} + {self.numero2} = {self.resul}')

    def subtracao(self):
        self. resul = self.numero1 - self.numero2
        print(f'{self.numero1} - {self.numero2} = {self.resul}')

    def multiplicar(self):
        self.resul = self.numero1 * self.numero2
        print(f'{self.numero1} X {self.numero2} = {self.resul}')


calculadora = Calculadora()
while True:
    print(''' ===== CALCULADORA =====
    [1] adição
    [2] subtração
    [3] multiplicar
    [4] Sair''')
    escolha = int(input('Sua opção: '))
    num = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    calculadora.numero1 = num
    calculadora.numero2 = num2
    print('Calculando....')
    sleep(4)
    if escolha == 1:
        calculadora.soma()
    elif escolha == 2:
        calculadora.subtracao()
    elif escolha == 3:
        calculadora.multiplicar()
    elif escolha == 4:
        break
    else:
        print('ERRO, ESCOLHA UMA OPÇÃO VALIDA')
