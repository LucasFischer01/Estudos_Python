print(' Conte quantas letras tem seu nome.\n')
nome = input('Insira seu primeiro nome: ')
qtd_char = len(nome)

if qtd_char <= 4:
    print(' Seu nome é curto.')
elif qtd_char <= 6:
    print(' Seu nome é normal.')
else:
    print(' Seu nome é muito grande.')