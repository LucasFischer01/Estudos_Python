# Exemplo prático de lista.

lista = ['string', 11, 23.5, True]
# índices    0        1     2      3
print(lista[3])

# Concatenação de listas.
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

# Extendendo Listas
l4 = [45, 46, 47]
l5 = [48, 49, 50]
l4.extend(l5)
print(l4)