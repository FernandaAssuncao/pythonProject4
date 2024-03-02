def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[1:31mERRO,digite um número inteiro valido!!!\033[m")
        if ok == True:
            break
    return valor


def leiafloat(msg):
    valor = 0
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print("\033[1:31mERRO,digite um valor real valido!!!\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[1:35mO usuario opitou não imformar o valor solicitado!!!\033[m")
            return 0
        else:
            return valor


def leiastr(msg):
    valor = ''
    while True:
        try:
            valor = str(input(msg))
        except:
            print("\033[1:31mDigite uma PALAVRA!!!\033[m")
        else:
            return valor


