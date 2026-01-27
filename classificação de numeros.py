from random import randint

lista = []
media = 0
for c in range(1, 11):
    lista.append(randint(1, 6))
for num in lista:
    media += num
maior = max(lista)
menor = min(lista)
print(f'O maior valor dos dados foi {maior}')
print(f'O menor valor dos dados foi {menor}')
print(f'E a media do valor foi {media / 2}')
