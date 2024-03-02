import tkinter as tk

janela = tk.Tk()

var_promocoes = tk.IntVar()
checkbos_promocoes = tk.Checkbutton(text='Deseja receber e-mail promocionais?', variable=var_promocoes)
checkbos_promocoes.grid(row=0, column=0)

var_politics = tk.IntVar()
check_politica = tk.Checkbutton(text='Você concorda com as politicas de privacidade?', variable=var_politics)
check_politica.grid(row=1, column=0)


def enviar():
    if var_promocoes.get():
        print('Usuario deseja receber promoções')
    else:
        print('Usuario NÃO deseja receber promoções')
    if var_politics.get():
        print('O usuario concordou com os termos de politicas de privacidade')
    else:
        print('O usuario NÃO concordou')


botao_enviar = tk.Button(text='Enviar', command=enviar)
botao_enviar.grid(row=2, column=0)


janela.mainloop()
