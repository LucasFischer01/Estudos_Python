""" FORMATANDO VALORES COM MODIFICADORES

:s - Textos (strings).
:d - Inteiros (int).
:f - Números de ponto flutuante (float).
:.(número)f - Quantidade de casas decimais.
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)

> - insere a variável a direita e os caracteres à esquerda.
< - insere a variável a esquerda e os caracteres à direita.
^ - insere a variável ao centro e os caracteres divididos à esquerda e à direita

"""

nome = 'lucas fischer'
idade = 25
altura = 1.7
print(f'{nome:s} {idade:d} {altura:f}')

# Definindo número de casas decimais.
num_1 = 13
num_2 = 15
aux = num_1 / num_2
print(f'{aux:.2f} {aux:.2}')#Fstring
print('{:.2}'.format(aux)) #Format

#Completando caracteres 
print(f'{nome:@>10}'), print('{:@>10}'.format(nome))
print(f'{nome:@<10}') 
print(f'{nome:@^10}') 

# Edição de impressão
nome_1 = 'lucas fischer'
print(nome_1.lower()) # Imprime todas as letras minúsculas
print(nome_1.upper()) # Imprime todas as letras maiúsculas
print(nome_1.capitalize())# imprime as primeiras letras maiúsculas
