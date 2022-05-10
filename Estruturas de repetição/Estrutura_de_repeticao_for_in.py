
 # exemplo de estrutura de repetição For.
texto = 'python'

for letra in texto:
    print(letra)

# Exemplo de iteração com For.
texto = 'python'
n_string = ''

for letra in texto:
    if letra == 'p':
        n_string = n_string + letra.upper()
    elif letra == 't':
        n_string += letra.upper()
    else:
        n_string += letra
print(n_string)