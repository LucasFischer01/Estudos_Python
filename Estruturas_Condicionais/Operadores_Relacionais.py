# exercício utilizando Estrutura Condicional e Operadores relacionais
nome = input(' Qual o seu nome? ')
idade = int(input(' Qual a sua idade? '))
idade_min = 18
if idade >= idade_min:
    print(f'{nome} pode solicitar empréstimo. ')
else:
    print(f'{nome} não pode solicitar empréstimo. ')
