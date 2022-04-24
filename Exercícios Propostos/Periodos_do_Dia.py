h = input(" Insira a hora correta: ")
minutos = input(" Insira os minutos:")

if h.isnumeric() and minutos.isnumeric():
    h = int(h)
    minutos = int(minutos)
    if h > 0 and (h <= 11 and minutos <= 59):
        print(f'Bom dia, são {h}:{minutos}.')
    elif h > 11 and (h <= 17 and minutos <= 59):
        print(f'Boa tarde, são {h}:{minutos}.')
    elif h > 17 and (h <= 23 and minutos <= 59):
        print(f'Boa noite, são {h}:{minutos}.')
    else:
        print('Insira números válidos.')
else:
    print('Insira números válidos.')
