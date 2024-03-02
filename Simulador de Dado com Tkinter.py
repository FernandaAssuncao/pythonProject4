from random import randint
import tkinter as tk


class SimuladorDeDado:
    def __init__(self):
        self.dado = None
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0
        self.num6 = 0

    def vefificar(self):
        if self.dado == 1:
            self.num1 += 1
        elif self.dado == 2:
            self.num2 += 1
        elif self.dado == 3:
            self.num3 += 1
        elif self.dado == 4:
            self.num4 += 1
        elif self.dado == 5:
            self.num5 += 1
        elif self.dado == 6:
            self.num6 += 1

    def mudar_texto(self):
        n1['text'] = f'1º {self.num1}'
        n2['text'] = f'2º {self.num2}'
        n3['text'] = f'3º {self.num3}'
        n4['text'] = f'4º {self.num4}'
        n5['text'] = f'5º {self.num5}'
        n6['text'] = f'6º {self.num6}'

    def girar_dado(self):
        self.dado = randint(1, 6)
        dado['text'] = f'O número que caiu foi {self.dado}'
        self.vefificar()
        self.mudar_texto()


janela = tk.Tk()
simulador = SimuladorDeDado()
janela.title('')
janela.configure(bg='#FFDEAD')

titulo = tk.Label(text='Simulador de Dado', borderwidth=4, relief='raised', bg='#FF7F50', fg='white',
                  font='Arial 15 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

dado = tk.Label(text='', bg='#FFA07A', fg='black', font='Arial 9 bold')
dado.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_girar_dado = tk.Button(text='Girar Dado', bg='#FF7F50', fg='white', font='Arial 10 bold',
                             command=simulador.girar_dado)
botao_girar_dado.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

titulo1 = tk.Label(text='Quantidade de vezes que cairam', borderwidth=4, relief='ridge', bg='#FF7F50',
                   fg='white', font='Arial 10 bold')
titulo1.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

n1 = tk.Label(text='1º', bg='#FFA07A', fg='white', font='Arial 9 bold')
n1.grid(row=3, column=1, padx=10, pady=10, sticky='nswe')

n2 = tk.Label(text='2º', bg='#FFA07A', fg='white', font='Arial 9 bold')
n2.grid(row=4, column=1, padx=10, pady=10, sticky='nswe')

n3 = tk.Label(text='3º', bg='#FFA07A', fg='white', font='Arial 9 bold')
n3.grid(row=5, column=1, padx=10, pady=10, sticky='nswe')

n4 = tk.Label(text='4º', bg='#FFA07A', fg='white', font='Arial 9 bold')
n4.grid(row=6, column=1, padx=10, pady=10, sticky='nswe')

n5 = tk.Label(text='5º', bg='#FFA07A', fg='white', font='Arial 9 bold')
n5.grid(row=7, column=1, padx=10, pady=10, sticky='nswe')

n6 = tk.Label(text='6º', bg='#FFA07A', fg='white', font='Arial 9 bold')
n6.grid(row=8, column=1, padx=10, pady=10, sticky='nswe')

janela.mainloop()
