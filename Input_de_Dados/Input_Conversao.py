# Input de dados com conversão de tipo de variável

nome = input('Qual é o seu nome? ')
idade = input('Qual sua idade? ')
a_nasc = 2022 - int(idade)

print(f'\n{nome} tem {idade} anos. '
      f'{nome} nasceu em {a_nasc}.')
