#Índices.
#       0123456789.......................33 
frase ='o rato roeu a roupa do rei de roma' #valor com índices = valor Iterável.
str_size = len(frase)
count = 0
nova_string = ''

l_maiuscula = input('Qual letra deseja colocar em letra maiúscula? ')

#Iteração - Iterar a string.
while count < str_size:
    letra = frase[count]
    if letra == l_maiuscula:
        nova_string += l_maiuscula.upper()
    else:
        nova_string += letra
    count +=1
print(nova_string)