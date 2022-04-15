# Utilização da função LEN para contabilização de caracteres.
nome_usuario = input( "Informe seu Usuário: ")
qtd_char = len(nome_usuario)
print(f'O usuário informado {nome_usuario} possui {qtd_char} caracteres do tipo {type(qtd_char)}')

# Soma de carateres de strings diferentes.
nome = input('Digite seu primeiro nome:')
sobrenome = input('Digite seu sobrenome:')
qtd_char1 = (len(nome)) + (len(sobrenome))

print(f'Seu nome {nome} {sobrenome} possui {qtd_char1} caracteres.')