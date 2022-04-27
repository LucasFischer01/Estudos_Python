# Índice positivo da String.
texto = "O rato roeu a roupa do rei de Roma."
print(texto[3])

# Índice negativo da String.
site = 'www.google.com.br/'
print(site[:-1])

# Fatiamento da string.
# Determinando Início e Fim.
nova_string = texto[2:7]
print(nova_string)
# Determinando apenas o Fim.
nova_string = texto[:11]
print(nova_string)
# Determinando o Passo.
nova_string = texto[::2]
print(nova_string)