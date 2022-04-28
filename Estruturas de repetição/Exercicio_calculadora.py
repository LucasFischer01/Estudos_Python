def to_number(x):
    if "." in x:
        return float(x)
    else:
        return int(x)

def calculadora():        
    while True:
        num_1 = input('Digite o primeiro número: ')
        num_2 = input('Digite o segundo número: ')
        if not num_1.isnumeric() or not num_2.isnumeric():
            print('Digite um número válido')
            calculadora()
        while True:
            num_1 = to_number(num_1)
            num_2 = to_number(num_2)
            op = input('Digite o operador: (+, -, / ou *): ')
            if op == '+':
                x = num_1 + num_2
            elif op == '-':
                x = num_1 - num_2
            elif op == '*':
                x = num_1 * num_2
            elif op == '/':
                x = num_1 / num_2
            else:
                print('Insira um operador válido')
                continue
            break
        if type(x) == float:
            x = round(x, 2)
        print(f'O resultado da operação {num_1}{op}{num_2} é igual a {x}')
        master = input('Deseja continuar?(s/n):')
        if master == 's':
            continue
        elif master == 'n':
            break
        else:
            print('Opção inválida, encerrando operações.')
            break
    print('Fim de operações, obrigado.')

calculadora()
