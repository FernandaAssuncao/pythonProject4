from random import randint
import tkinter as tk


janela = tk.Tk()
janela.title('')
janela.configure(bg='#FFC0CB')

titulo = tk.Label(text='Gerador de Matrix', bg='#FFB6C1', borderwidth=4, relief='raised', fg='white',
                  font='Arial 20 bold')
titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nswe')

mensagem = tk.Label(text='', bg='#FFC0CB', fg='white', font='Arial 12 bold')
mensagem.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

botao_gerar_matrix = tk.Button(text='Gerar Matrix', bg='#FFB6C1', fg='white', font='Arial 15 bold')
botao_gerar_matrix.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')


janela.mainloop()
