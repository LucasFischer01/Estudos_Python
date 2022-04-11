nome = 'Lucas'
idade = 25
altura = 1.70
peso = 65
imc = peso / altura**2
# exemplo sem a formatação.
print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
# exemplo de formatação de string com função FString.
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
# exemplo de formatação format
print('{0} tem {1} anos de idade e seu IMC é {2:.2f}'.format(nome, idade, imc))
# exemplo de formatação format com parâmetros nomeados
print('{n} tem {i} anos de idade e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc))
