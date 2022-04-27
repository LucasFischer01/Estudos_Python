aux = True
while aux == True:
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Digite um número válido')
        continue
    num_1 = float(num_1) 
    num_2 = float(num_2)
    aux_op = True
    while aux_op == True:
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
            aux_op = True
            continue
        aux_op = False
    print(f'O resultado da operação {num_1}{op}{num_2} é igual a {x:.2}')
    master = input('Deseja continuar?(s/n):')
    if master == 's':
        aux = True
    elif master == 'n':
        aux = False
    else:
        print('Opção inválida, encerrando operações.')
        aux = False
print('Fim de operações, obrigado.')



