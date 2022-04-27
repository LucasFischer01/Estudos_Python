# Exemplificando o laço de repetição WHILE
aux = 0
while aux <= 10:
    print(aux)
    aux = aux + 1

# Laço WHILE com continue.
aux1 = 0
while aux1 <= 10:
    if aux1 == 3:
        aux1 = aux1 + 1
        continue
    print(aux1)
    aux1 = aux1 + 1
print('FIM.')

# Laço WHILE com break
aux1 = 0
while aux1 <= 10:
    if aux1 == 3:
        aux1 = aux1 + 1
        break
    print(aux1)
    aux1 = aux1 + 1
print('FIM.')
