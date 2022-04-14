# Exemplificação dos operadores lógicos. AND - OR - NOT - IN - NOT IN.

# Operador And.
num_1 = 5
num_2 = 4
if num_1 > num_2 and num_1 != num_2:
    print('Válido.')
else:
    print('Invalido.')

# Operador OR.
num_3 = 6
num_4 = 4
if num_3 == 6 or num_4 < num_3:
    print('Válido.')
else:
    print('Invalido.')

# Operador NOT.
num_5 = 6
if not num_5 == 5:
   print('Válido.')
else:
    print('Invalido.')

# Operador In.
nome = " Geronimo Silva "
if "imo" in nome:
    print