print('Números Pares e Ímpares.\n')
num1 = input('Insira o número desejado: ')

if num1.isnumeric():
    num1 = int(num1)
    aux = num1 % 2
    if aux == 0:
        print(f"O número {num1} é Par.")
    else:
        print(f'O número {num1} é Ímpar.')
else:
    print('Insira um número inteiro válido para a operação.')
