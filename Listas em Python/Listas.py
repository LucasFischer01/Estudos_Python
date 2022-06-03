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

# Adicionando variáveis ao final da lista.
l6 = [1, 'a', 2]
print(l6)
l6.append('novo elemento')
print(l6)

# Adicionando variáveis em um índice desejado.
la = ['a', 'b', 'c']
print(la)
la.insert(0, 'd')
print(la)

# Excluindo a última variável da lista.
la.pop()
print(la)

# Excluindo variáveis da lista através do fatimamento.
lb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     0  1  2  3  4  5  6  7  8  9   índices
print(lb)
del(lb[2:5])
print(lb)

# classificando valor mínimo e valor máximo.
lc = [0, 1, 2, 3, 15, 4, 5, 6, 7, 8, 9]
print(max(lc))
print(min(lc))

# utilização função List + range.
ld = list(range(1, 10))
print(ld)
