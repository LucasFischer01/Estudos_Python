nome = 'Lucas'
idade = 26
altura = 1.70
peso = 65
a_at = 2022
a_nasc = a_at - idade
imc = peso / altura**2
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {a_nasc}.')

